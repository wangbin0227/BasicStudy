# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-05-28 00:11:40
# @FileName: calendar_func

import os
import sys

import calendar

def format_cal():
    cal = calendar.TextCalendar()
    cal.prmonth(2020, 5)

    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal.prmonth(2020, 5)

def calendar_func():
    """
    Args:
    Returns:
    Raises:
    """
    format_cal()

if __name__ == "__main__":
    calendar_func()
