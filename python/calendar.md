calendar模块定义了Calendar类，该类封装了给定月份或者年份计算周日期的方法。此外，TextCalendar和HTMLCalendar类 可以生成预格式化的输出。

```
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
```

