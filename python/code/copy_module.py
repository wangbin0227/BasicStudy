# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-06-05 22:16:18
# @FileName: copy_module

import os
import sys
import copy

class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

    def __copy__(self):
        print ('__copy__()')
        return MyClass(copy.copy(self.name))

    def __deepcopy__(self, memo):
        print ('__deepcopy__({})'.format(memo))
        return MyClass(copy.deepcopy(self.name, memo))

def shallow_copy():
    a = MyClass('a')
    cur_list = [a]
    dup_list = copy.copy(cur_list)
    print ('cur_list:', cur_list)
    print ('dup_list:', dup_list)
    print ('cur_list is dup_list:', cur_list is dup_list)
    print ('cur_list == dup_list:', cur_list == dup_list)
    print ('cur_list[0] is dup_list[0]:', cur_list[0] is dup_list[0])
    print ('cur_list == dup_list:', cur_list[0] == dup_list[0])

def deep_copy():
    a = MyClass('a')
    cur_list = [a]
    dup_list = copy.deepcopy(cur_list)
    print ('cur_list:', cur_list)
    print ('dup_list:', dup_list)
    print ('cur_list is dup_list:', cur_list is dup_list)
    print ('cur_list == dup_list:', cur_list == dup_list)
    print ('cur_list[0] is dup_list[0]:', cur_list[0] is dup_list[0])
    print ('cur_list == dup_list:', cur_list[0] == dup_list[0])

def customizing_copy():
    a = MyClass('a')
    sa = copy.copy(a)
    da = copy.deepcopy(a)
    print (a, sa, da)


class Graph:

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return 'Graph(name={}, id={})'.format(
            self.name, id(self))

    def __deepcopy__(self, memo):
        print('\nCalling __deepcopy__ for {!r}'.format(self))
        if self in memo:
            existing = memo.get(self)
            print('  Already copied to {!r}'.format(existing))
            return existing
        print('  Memo dictionary:')
        if memo:
            for k, v in memo.items():
                print('    {}: {}'.format(k, v))
        else:
            print('    (empty)')
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print('  Copying to new object {}'.format(dup))
        memo[self] = dup
        for c in self.connections:
            print ('----{}----{}'.format(self.name, c))
            dup.add_connection(copy.deepcopy(c, memo))
        return dup

def recursion_deepcopy():
    root = Graph('root', [])
    a = Graph('a', [root])
    b = Graph('b', [a, root])
    root.add_connection(a)
    root.add_connection(b)
    dup = copy.deepcopy(root)


def copy_module():
    """
    Args:
    Returns:
    Raises:
    """
    recursion_deepcopy()
    return
    customizing_copy()
    return
    deep_copy()
    shallow_copy()

if __name__ == "__main__":
    copy_module()
