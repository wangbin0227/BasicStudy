# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2021-05-28 19:53:11
# @FileName: argparse_module

import os
import sys
import argparse





def argparse_module():
    """
    Args:
    Returns:
    Raises:
    """
    parser = argparse.ArgumentParser(prog="Test")
    parser.add_argument('--foo')
    parser.add_argument('--test', type=str, default="", help="test data")
    FLAGS, unparsed = parser.parse_known_args()
    print (FLAGS)
    print (unparsed)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Test")
    parser.add_argument('--foo')
    parser.add_argument('--test', type=str, default="", help="test data")
    FLAGS, unparsed = parser.parse_known_args()
    print (FLAGS)
    print (unparsed)
    argparse_module()
