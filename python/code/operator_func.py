# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-05-24 14:18:00
# @FileName: operator_func

import os
import sys
from operator import *


def logical_operations():
    a = -1
    b = 5
    print ('a =', a)
    print ('b =', b)
    print ()

    print ('not_(a)     :', not_(a))
    print ('truth(a)    :', truth(a))
    print ('is_(a, b)   :', is_(a, b))
    print ('is_not(a, b):', is_not(a, b))


def comparison_operations():
    a = 1
    b = 5.0

    print ('a = ', a)
    print ('b = ', b)

    for func in (lt, le, eq, ne, gt, ge):
        print ('{}(a, b): {}'.format(func.__name__, func(a, b)))

def arithmetic_operations():
    a = -1
    b = 5.0
    c = 2
    d = 6

    print ("Positive/Negative")
    print ('abs(a):', abs(a))
    print ('neg(b):', neg(b))
    print ('pos(c):', pos(c))

    print ("\nArithmetic")
    print ("add(a, b)      :", add(a, b))
    print ("sub(b, a)      :", sub(b, a))
    print ("mul(a, b)      :", mul(a, b))
    print ("floordiv(a, b) :", floordiv(a, b))
    print ("truediv(a, b)  :", truediv(a, b))
    print ("floordiv(d, c) :", floordiv(d, c))
    print ("truediv(d, c)  :", truediv(d, c))
    print ("mod(a, b)      :", mod(a, b))
    print ("pow(c, d)      :", pow(c, d))

    print ("\nBitwise")
    print ("and_(c, d)", and_(c, d))
    print ("invert(c)", invert(c))
    print ("lshift(c, d)", lshift(c, d))
    print ("or_(c, d)", or_(c, d))
    print ("rshift(d, c)", rshift(d, c))
    print ("xor(c, d)", xor(c, d))

def sequence_operations():
    a = [1, 2, 3]
    b = ['a', 'b', 'c', 'd']
    print ("Constructive")
    print ("concat(a, b): ", concat(a, b))

    print ("\nSearching")
    print ("contains(a, 1) :", contains(a, 1))
    print ("countOf(b, 'c'):", countOf(b, "c"))
    print ("countOf(b, 'd'):", countOf(b, "d"))
    print ("indexOf(a, 1)  :", indexOf(a, 1))


    print ("\nAccess Items")
    print ("getitem(b, 1) :", getitem(b, 1))
    print ("getitem(b, slice(1, 3)) :", getitem(b, slice(1, 3)))
    print ("setitem(b, 1, 'd') :", end = ' ')
    setitem(b, 1, "d")
    print (b)

    print ("\nDestructive")
    print (" delitem(b, 1) :", end=" ")
    delitem(b, 1)
    print (b)


def inplace_operations():
     a = -1
     b = 5.0
     c = [1, 2, 3]
     d = ['a', 'b', 'c']

     a = iadd(a, b)
     print ('a = iadd(a, b) =>', a)

     c = iconcat(c, d)
     print ('c = iconcat(c, d) =>', c)

class MyObj:
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

def getters_operations():

    ### attrgetter
    l = [MyObj(i) for i in range(5)]
    print ('objects :', l)

    g = attrgetter('arg')
    vals = [g(i) for i in l]
    print ('arg values:', vals)
    
    l.reverse()
    print (l)
    print ('sorted :', sorted(l, key=g))

    ### itemgetter
    l = [dict(val= -1 * i) for i in range(4)]
    print ('original: ', l)
    g = itemgetter('val')
    vals = [g(i) for i in l]
    print (values)


    


def operator_func():
    """
    Args:
    Returns:
    Raises:
    """
    getters_operations()
    inplace_operations()
    sequence_operation()
    arithmetic_operations()
    comparison_operations()
    logical_operations()


if __name__ == "__main__":
    operator_func()
