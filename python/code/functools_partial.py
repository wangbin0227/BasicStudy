# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-03-08 19:52:19
# @FileName: functools_partial

import os
import sys

def myfunc(a, b=2):
    print ("    called myfunc with: ", (a, b))

def show_detail(name, f, is_partial=False):
    print ("{}:".format(name))
    print ("    object: ", f)
    if not is_partial:
        print ("    __name__: ", f.__name__)
    else:
        print ("    func:", f.func)
        print ("    args:", f.args)
        print ("    keywords:", f.keywords)
    return

def functools_partial():
    import functools
    """
    Args:
    Returns:
    Raises:
    """
    show_detail('myfunc', myfunc)
    myfunc('a', 3)
    print()
    p1 = functools.partial(myfunc, b=4)
    show_detail('partial with named default', p1, True)
    p1("passing a")
    p1("override b", b=5)
    print()
    p2 = functools.partial(myfunc, "default a", b=99)
    show_detail('partial wite default', p2, True)
    p2()
    p2(b="override b")
    print ()

if __name__ == "__main__":
    functools_partial()
