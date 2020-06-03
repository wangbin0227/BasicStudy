queue模块提供了适合多线程编程的先进先出的数据结构，可以用来在生产者和消费者线程之间安全的传递消息或者数据；锁是调用方处理，因此多线程可以安全、方便的使用同一队列实现。

### FIFO 队列
Queue类，实现了最基础的先进先出队列，使用put方法，将元素添加到末尾，使用get方法将元素从另一边删除

```
def queue_fifo():
    q = queue.Queue()
    for i in range(5):
        q.put(i)

    while not q.empty():
        print (q.get(), end = ' ')
    print ()
```

### LIFO 栈
与标准的FIFO队列不同，LifoQueue实现了后进先出，这通常是栈；

```
def queue_lifo():
    q = queue.LifoQueue()
    for i in range(5):
        q.put(i)

    while not q.empty():
        print (q.get(), end = ' ')
    print ()

```

### 优先级队列
有时，队列中元素的处理顺序需要基于这些元素的特征，而不仅仅是添加到队列中的顺序。例如，财务部门的打印作业可能优先于开发人员的代码列表打印。PriorityQueue使用队列内容的排序顺序来决定要检索的元素。
 
```
class Job():
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print (description)
        return

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

def priority_queue():
    import threading
    print ('initial')
    q = queue.PriorityQueue()
    q.put(Job(5, 'Mid Job'))
    q.put(Job(10, 'Low Job'))
    q.put(Job(1, 'Imp Job'))

    def process_job(q):
        while True:
            next_job = q.get()
            print (next_job.description)
            q.task_done()
    workers = [
        threading.Thread(target=process_job, args=(q, )),
        threading.Thread(target=process_job, args=(q, )),
    ]
    print ('get')
    for w in workers:
        w.setDaemon(True)
        w.start()
    q.join()
```

### 构建多线程的播放客户端

   本节播放客户端的源代码演示Queue和多线程一起使用的场景。该程序读取一个或多个RSS 摘要，将每一个摘要中五个最新事件放入Queue中等待下载，使用多线程并行处理下载。该框架实现演示了queue模块的使用。

```
def podcast_client():
    ### 0. 初始化
    import threading
    num_fetch_threads = 2
    enclosure_queue = queue.Queue()
    feed_urls = [
        'http://talkpython.fm/episodes/rss',
    ]

    ### 1. 辅助函数打印信息
    def message(s):
        print ('{}: {}'.format(threading.current_thread().name, s))

    ### 2. 多线程目标函数函数
    def download_enclosures(q):
        import urllib
        message('looking for the next enclosure')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        message('writing to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()

    ### 3. 启动多线程
    for i in range(num_fetch_threads):
        worker = threading.Thread(
            target = download_enclosures,
            args = (enclosure_queue, ),
            name = 'work-{}'.format(i),
        )
        worker.setDaemon(True)
        worker.start()

    ### 4. 队列中添加URL
    import feedparser
    from urllib.parse import urlparse
    for url in feed_urls:
        response = feedparser.parse(url, agent='queue_module.py')
        for entry in response['entries'][:5]:
            for enclosure in entry.get('enclosures', []):
                parsed_url = urlparse(enclosure['url'])
                message('queuing {}'.format(
                    parsed_url.path.rpartition('/')[-1]))
                enclosure_queue.put(enclosure['url'])

    ### 5. 主线程
    message('*** main thread waiting')
    enclosure_queue.join()
    message('*** done')
```    

首先，进行参数初始化，确定操作参数：通常来自于用户输入。该示例使用硬编码值，表示要获取的线程数和URL列表，并创建用来打印信息的辅助函数message

在work线程中执行download\_enclosures方法，使用urllib处理下载。
线程中定义了目标函数后，就可以启动工作：download\_enclosures方法中，语句url=q.get()执行时，会阻塞并等待队列返回内容，这意味着在队列没有任何内容之前启动线程是安全的。

下一步是使用feedparser模块(需要安装)检索摘要内容，并将url插入到队列中。一旦URL被添加到队列中，线程就会将其读取并开始下载，循环往队列中添加元素，直到摘要消耗完，工作线程轮流讲url出队列下载。
