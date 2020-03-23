# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-03-08 21:50:19
# @FileName: functools_partial

import os
import sys

def myfunc(a, b=2):
    print ("    called myfunc with: ", (a, b))

def show_detail(name, f):
    print ("{}:".format(name))
    print ("    object: ", f)
    print ("    __name__:", end="   ")
    try:
        print (f.__name__)
    except AttributeError:
        print ("(no __name__)")
    print ("    __doc__", repr(f.__doc__))

def functools_partial():
    import functools
    """
    Args:
    Returns:
    Raises:
    """
    show_detail('myfunc', myfunc)
    p1 = functools.partial(myfunc, b=4)
    show_detail('raw wrapper', p1)

    p2 = functools.update_wrapper(p1, myfunc)
    show_detail('update wrapper', p2)

if __name__ == "__main__":
    functools_partial()
