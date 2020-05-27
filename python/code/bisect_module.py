# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-05-28 00:23:54
# @FileName: bisect_module

import os
import sys

import bisect


def bisect_module():
    """
    Args:
    Returns:
    Raises:
    """
    values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

    new_list = []
    print ('Val POS Current')
    for i in values:
        pos = bisect.bisect(new_list, i)
        bisect.insort(new_list, i)
        print ("{:3} {:3}".format(i, pos,), new_list)

    new_list = []
    print ('Val POS Current')
    for i in values:
        pos = bisect.bisect_left(new_list, i)
        bisect.insort_left(new_list, i)
        print ("{:3} {:3}".format(i, pos,), new_list)

if __name__ == "__main__":
    bisect_module()
