queue模块提供了适合多线程的


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
首先，确定操作参数：通常来自于用户输入。本节示例使用硬编码值，表示要获取的线程数和URL列表。

在work线程中执行download_enclosures方法，使用urllib处理下载。