# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-05-24 14:18:00
# @FileName: operator_func


import os
import sys
import time


def clock_basic():
    import textwrap
    available_clocks = [
        ('time', time.time),
        ('monotonic', time.monotonic),
        ('perf_counter', time.perf_counter),
        ('process_time', time.process_time),
    ]

    for clock_name, func in available_clocks:
        print (
            textwrap.dedent('''
            {name}:
                adjustable    :{info.adjustable}
                implementation:{info.implementation}
                monotonic     :{info.monotonic}
                resolution    :{info.resolution}
                current       :{current}'''.format(name=clock_name, info=time.get_clock_info(clock_name), current=func())
            )
        )

def clock_time():
    print (time.time())
    print (time.ctime())

def clock_monotonic():
    start = time.monotonic()
    time.sleep(0.1)
    end = time.monotonic()
    print (start)
    print (end)

def processor_clock():
    template = '{} - {:.2f} - {:.2f}'
    print (template.format(time.ctime(), time.time(), time.process_time()))

    for i in range(3, 0, -1):
        time.sleep(i)
        print (template.format(time.ctime(), time.time(), time.process_time()))

def perf_counter_clock():
    loop_start = time.perf_counter()

    for i in range(5):
        iter_start = time.perf_counter()
        a = 1
        for i in range(10000):
            a = a + i
        now = time.perf_counter()
        loop_elapsed = now - loop_start
        iter_elapsed = now - iter_start
        print ('{:.6f} {:.6f}'.format(loop_elapsed, iter_elapsed))

def time_func():
    """
    Args:
    Returns:
    Raises:
    """
    perf_counter_clock()
    return
    processor_clock()
    return
    clock_monotonic()
    return
    clock_time()
    return
    clock_basic()


if __name__ == "__main__":
    time_func()
