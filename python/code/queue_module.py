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


    


def queue_module():
    """
    Args:
    Returns:
    Raises:
    """
    priority_queue()
    return
    queue_lifo()
    return
    queue_fifo()

if __name__ == "__main__":
    queue_module()
