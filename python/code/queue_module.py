# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-06-02 00:13:46
# @FileName: queue_module

import os
import sys
import queue

def queue_fifo():
    q = queue.Queue()
    for i in range(5):
        q.put(i)

    while not q.empty():
        print (q.get(), end = ' ')
    print ()

def queue_lifo():
    q = queue.LifoQueue()
    for i in range(5):
        q.put(i)

    while not q.empty():
        print (q.get(), end = ' ')
    print ()

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


def podcast_client():
    ### 初始化
    import threading
    num_fetch_threads = 2
    enclosure_queue = queue.Queue()
    feed_urls = [
        'http://talkpython.fm/episodes/rss',
    ]

    ### 辅助函数打印信息
    def message(s):
        print ('{}: {}'.format(threading.current_thread().name, s))

    ### 多线程目标函数函数
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

    ### 启动多线程
    for i in range(num_fetch_threads):
        worker = threading.Thread(
            target = download_enclosures,
            args = (enclosure_queue, ),
            name = 'work-{}'.format(i),
        )
        worker.setDaemon(True)
        worker.start()

    ### 队列中添加URL
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

    ### 主线程
    message('*** main thread waiting')
    enclosure_queue.join()
    message('*** done')

def queue_module():
    """
    Args:
    Returns:
    Raises:
    """
    podcast_client()
    return
    priority_queue()
    return
    queue_lifo()
    return
    queue_fifo()

if __name__ == "__main__":
    queue_module()
