# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-05-28 10:22:43
# @FileName: collections_module

import os
import sys

import collections

def counter_container():
    cur_counter = collections.Counter
    print (cur_counter(['a', 'b', 'c', 'd', 'a', 'a', 'b']))
    print (cur_counter({'a':3, 'b': 2, 'c': 1, 'd': 1}))
    print (cur_counter(a=3, b=2, c=1, d=1))

    cur_counter_demo = collections.Counter()
    cur_counter_demo.update('abcda')
    print (cur_counter_demo)
    cur_counter_demo.update({'a':3, 'd':4})
    print (cur_counter_demo)

def counter_access():
    cur_counter_demo = collections.Counter(['a', 'b', 'c', 'd', 'a', 'a', 'b'])
    for letter in 'abcdef':
        print ('{} : {}'.format(letter, cur_counter_demo[letter]))

    cur_counter_demo['z'] = 0
    print (cur_counter_demo)
    print (list(cur_counter_demo.elements()))


    print (cur_counter_demo.most_common(2))

def counter_arith():
    counter_1 = collections.Counter(['a', 'b', 'a', 'c', 'b', 'a'])
    counter_2 = collections.Counter({'a':2, 'c':2, 'd':1})
    print ('counter_1: ', counter_1)
    print ('counter_2: ', counter_2)

    print ('add: ', counter_1 + counter_2 )
    print ('sub: ', counter_1 - counter_2)
    print ('&: ', counter_1 & counter_2)
    print ('|: ', counter_1 | counter_2)

def collections_module():
    """
    Args:
    Returns:
    Raises:
    """
    counter_arith()
    return
    counter_access()
    return
    counter_container()

if __name__ == "__main__":
    collections_module()
