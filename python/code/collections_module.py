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

def defaultdict_module():
    def _default_factory(value):
        return lambda : value
    d = collections.defaultdict(_default_factory('default_value'))
    print (d['unknown'])

    d = collections.defaultdict(list)
    print (d['test'])

    d = collections.defaultdict(int)
    print (d['test'])

def namedtuple_module():
    Person = collections.namedtuple('Person', 'name age')
    p = Person(name='Bob',age=21)
    print (p)
    print (p.name)
    print (p[1])

    try:
        Person = collections.namedtuple('Person', 'name class age')
    except ValueError as err:
        print (err)

    try:
        Person = collections.namedtuple('Person', 'name age age')
    except ValueError as err:
        print (err)

    Person = collections.namedtuple('Person', 'name age age', rename=True)
    print (Person._fields)
    p = Person(name='Bob', age=21, _2=22)
    print (p)

def ordered_dict_module():
    d = {}
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    for k, v in d.items():
        print (k, v)
    d = collections.OrderedDict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    for k, v in d.items():
        print (k, v)

    d.move_to_end('b')
    print ('move end')
    for k, v in d.items():
        print (k, v)

    d.move_to_end('c', last=False)
    print ('move first')
    for k, v in d.items():
        print (k, v)

def chain_map_module():
    a = {'a': 1, 'c': 3}
    b = {'b': 2, 'c': 4}
    m = collections.ChainMap(a,b)
    print (m)
    for k, v in m.items():
        print (k, v)
    print (m['c'])

    print (m.maps)
    m.maps = list(reversed(m.maps))
    print (m['c'])
    m.maps.append({'e': 5})
    print (m.maps)
    print (m['e'])

def chain_map_update():
    a = {'a': 1, 'c': 3}
    b = {'b': 2, 'c': 4}
    m = collections.ChainMap(a,b)
    print (m['c'])
    a['c'] = 5
    print (m['c'])

    m['c'] = 6
    print (a)

    m2 = m.new_child()
    m2['c'] = 100
    print (m2)

def deque_module():
    d = collections.deque()
    d.extend('abcdefg')
    print (d)
    d.append('h')
    print (d)

    d = collections.deque()
    d.extendleft('abcdefg')
    print (d)
    d.appendleft('h')
    print (d)

    d = collections.deque(range(5))
    print (d)
    print (d.pop())
    print (d.popleft())

    d = collections.deque(maxlen=3)
    d2 = collections.deque(maxlen=3)
    for i in range(5):
        print ('---- {} ---- '.format(i))
        d.append(i)
        d2.appendleft(i)
        print (d)
        print (d2)


def collections_module():
    """
    Args:
    Returns:
    Raises:
    """
    deque_module()
    chain_map_update()
    chain_map_module()
    ordered_dict_module()
    namedtuple_module()
    defaultdict_module()
    counter_arith()
    counter_access()
    counter_container()

if __name__ == "__main__":
    collections_module()
