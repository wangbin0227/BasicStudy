bisect模块实现了将元素插入列表中，同时保持列表有序的算法。

对于短列表而言，构建列表后直接排序可能更快，但是对于长列表使用这样的插入算法，可以节省大量的时间和内存，尤其是两个元素的比较操作需要昂贵的计算。



```
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
```