# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-06-01 14:30:24
# @FileName: array_module

import os
import sys
import array

def array_initial():
    a = array.array('b', b'abcdefg')
    print (a)

    a = array.array('i', range(3))
    print (a)
    a.extend(range(3))
    print (a)
    print (list(enumerate(a)))

def array_file():
    import tempfile
    import binascii
    a = array.array('i', range(5))
    print ('A1:', a)
    output = tempfile.NamedTemporaryFile()
    a.tofile(output.file)
    print (output.name)
    output.flush()
    print (output.name)
    with open(output.name, 'rb') as input:
        raw_data = input.read()
        print ('Raw:',binascii.hexlify(raw_data))

        input.seek(0)
        a2 = array.array('i')
        a2.fromfile(input, len(a))
        print ('A2:', a2)

def array_module():
    """
    Args:
    Returns:
    Raises:
    """
    array_file()
    return
    array_initial()

if __name__ == "__main__":
    array_module()
