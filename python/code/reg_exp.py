# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-03-19 21:59:14
# @FileName: reg_exp

import os
import sys
import re

def re_match():
    pattern = "this"
    text = "Does this text match"
    match = re.search(pattern, text)
    start = match.start()
    end = match.end()
    print ("Found {} \nin {} \nfrom {} to {}".format(match.re.pattern, match.string, start, end))

    regex_list = [
        re.compile(p) for p in ['this', 'that']
    ]

    for regex in regex_list:
        print ("Seeking '{}' ->".format(regex.pattern), end = "  ")
        if regex.search(text):
            print ("match")
        else:
            print ("no match")

def re_mul_match():
    text = "abaaaabbaaaa"
    pattern = r'(a)(ab|ac)'
    for match in enumerate(re.findall(pattern, text)):
        print ("found {}".format(match))


    for match in re.finditer(pattern, text):
        print (match)

def test_patterns():
    def show(text, patterns):
        for pattern, desc in patterns:
            print ("'{}' ({}) ".format(pattern, desc))
            print ("    {}".format(text))
            for match in re.finditer(pattern, text):
                start = match.start()
                end = match.end()
                substr = text[start: end]
                n_backslashes = text[: start].count("\\")
                prefix = "." * (start + n_backslashes)
                print ("    {}{}".format(prefix, substr))
            print ()


    text = 'abbaaabbbbaaaaa'
    patterns = [('ab', "a followed by b")]
    show(text, patterns)

    text = 'abbaabbba'
    ### 重复： 贪心
    patterns = [
        ('ab*', 'a followed by zero or more b'),
        ('ab+', 'a followed by one or more b'),
        ('ab?', 'a followed by zero or one b'),
        ('ab{3}', 'a followed by three b'),
        ('ab{2,3}', 'a followed by two to three b')
    ]
    show(text, patterns)

    ## 重复：关闭贪心
    patterns = [
        ('ab*?', 'a followed by zero or more b'),
        ('ab+?', 'a followed by one or more b'),
        ('ab??', 'a followed by zero or one b'),
        ('ab{3}?', 'a followed by three b'),
        ('ab{2,3}?', 'a followed by two to three b')
    ]
    show(text, patterns)

    ## 字符集: 包括
    text = 'abbaaabbba'
    patterns = [
        ('[ab]', 'either a or b'),
        ('a[ab]+', 'a followed by one or more a or b'),
        ('a[ab]+?', 'a followed by one or more a or b, not greedy'),
        ('a[ab]', 'a followed by one or more a or b'),
    ]
    show(text, patterns)

    ## 字符集: 不包括
    text = "This is some text -- with punctuation"
    patterns = [
        ('[^-. ]+', 'sequences without -, ., space')
    ]
    show(text, patterns)

    ## 字符集: 区间
    text = "This is some text -- with punctuation"
    patterns = [
        ('[a-z]+', 'sequences of lowercase letters'),
        ('[A-Z]+', 'sequences of uppercase letters'),
        ('[a-zA-Z]+', 'sequences of letters'),
        ('[A-Z][a-z]+', 'one uppercase followed by lowercase'),
    ]
    show(text, patterns)

    ## 字符集: 任意字符
    text = 'abbaaabbba'
    patterns = [
        ('a.*b', 'a followed by anything, ending in b'),
        ('a.*?b', 'a followed by anything, ending in b, not greedy'),
    ]
    show(text, patterns)

    ## 字符集: 转义字符
    text = "A prime #1 example!"
    patterns = [
        (r'\d+', 'sequence of digits'),
        (r'\D+', 'sequence of non-digits'),
        (r'\s+', 'sequence of whitespace'),
        (r'\S+', 'sequence of non-whitespace'),
        (r'\w+', 'alphanumeric characters'),
        (r'\W+', 'non-alphanumeric characters'),
    ]
    show(text, patterns)

    ## 位置标记
    text = "This is some text -- with punctuation."
    patterns = [
        (r'^\w+', 'word at start of string'),
        (r'\w+\S*$', 'word at start of string'),
    ]
    show(text, patterns)

def test_match_method():
    text = "abcd"
    pattern = "bc"
    print (re.search(pattern, text))
    print (re.match(pattern, text))
    print (re.fullmatch(pattern, text))

    pattern = "ab"
    print (re.match(pattern, text))
    print (re.fullmatch(pattern, text))

    pattern = "abcd"
    print (re.match(pattern, text))
    print (re.fullmatch(pattern, text))

def groups_match():
    text = "This is some text -- with punctuation."
    patterns = [
        (r'(\bt\w+)\W+(\w+)', 'word at start of string'),
    ]
    for pattern, desc in patterns:
        reg_exp = re.compile(pattern)
        match = reg_exp.search(text)
        print (match, match.groups())
        print (match.groupdict())

    patterns = [
        (r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)', 'word at start of string'),
    ]
    for pattern, desc in patterns:
        reg_exp = re.compile(pattern)
        match = reg_exp.search(text)
        print (match, match.groups())
        print (match.groupdict())

def test_sub():
    text = 'Make this **bold**. This **too**.'
    bold = re.compile(r'\*{2}(.*?)\*{2}')
    print ('Bold:', bold.sub(r'<b>\1</b>', text))
    print ('Bold:', bold.sub(r'<b>\1</b>', text, count=1))
    print ('Bold:', bold.subn(r'<b>\1</b>', text))

def test_split():
    text = "asssbbssdd"
    pattern = r'(\w+?)(s{2,}|$)'
    for num, para in enumerate(re.findall(pattern, text)):
        print (num, para)
    print ()

    for num, para in enumerate(re.split(r's{2,}', text)):
        print (num, para)
    print ()

    for num, para in enumerate(re.split(r'(s{2,})', text)):
        print (num, para)
    print ()

    

def reg_exp():
    """
    Args:
    Returns:
    Raises:
    """
    test_split()
    return
    test_sub()
    return
    groups_match()
    return
    test_match_method()
    return
    re_mul_match()
    return
    test_patterns()
    return
    return
    re_match()

if __name__ == "__main__":
    reg_exp()
