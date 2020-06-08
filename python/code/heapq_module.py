# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-06-08 20:46:45
# @FileName: heapq_module

import os
import sys


def show_tree(tree, total_width=36, fill = ' '):
    import math
    from io import StringIO
    output = StringIO()
    last_row = -1
    for i, value in enumerate(tree):
        row = int(math.floor(math.log(i + 1, 2)))
        if row != last_row:
            output.write('\n')
        cur_width = int(math.floor(total_width / (2 ** row)))
        output.write(str(value).center(cur_width, fill))
        last_row = row
    print (output.getvalue())
    print('-' * total_width)
    print()
        

def heapq_module():
    """
    Args:
    Returns:
    Raises:
    """
    show_tree([1,2,3,4,5,6,7,8,9])

if __name__ == "__main__":
    heapq_module()
