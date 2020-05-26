
# -*- coding:utf-8 -*-
# @Author: wangbin
# @Time: 2020-05-24 14:18:00
# @FileName: operator_func

import datetime

def time_study():
    t = datetime.time()
    print (t)

    t = datetime.time(0, 2, 3)
    print (t)

    t = datetime.time(1, 2, 3, microsecond=2)
    print (t)
    print (t.microsecond)
    print (t.tzinfo)

    print ("Earliest  :", datetime.time.min)
    print ("Latest    :", datetime.time.max)
    print ("Resolution:", datetime.time.resolution)

def date_study():
    date = datetime.date(1, 1, 1)
    print (date)
    print (date.toordinal())

    import time
    ts = time.time()
    date = datetime.date.fromtimestamp(ts)
    print (date)

    date = datetime.date.today()
    print (date)
    date_2 = date.replace(year=2019)
    print (date_2)


    today = datetime.date.today()
    print (today)
    print ('ctime :', today.ctime())
    print ('ordinal:', today.toordinal())
    tt = today.timetuple()
    print ('timetuple: tm_year = ', tt.tm_year)


    print ("Earliest  :", datetime.date.min)
    print ("Latest    :", datetime.date.max)
    print ("Resolution:", datetime.date.resolution)

def timedelta_study():
    print ('hours: ', datetime.timedelta(hours=10))
    print ('days: ', datetime.timedelta(days=1, seconds=100))

    delta = datetime.timedelta(days=1, seconds=100)
    print ('total seconds: ', delta.total_seconds())


def date_arithmetic_study():

    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)

    yesterday = today - one_day
    tommorow = today + one_day

    print ('today: ', today)
    print ('yesterday: ', yesterday)
    print ('tommorow: ', tommorow)
    
    print ('tommorow - yesterday: ', tommorow - yesterday)
    

def date_compare_study():

    t_1  = datetime.time(1, 2, 3)
    t_2 = datetime.time(4, 5, 6)
    print (t_1)
    print (t_2)
    print ('t_1 < t_2 :', t_1 < t_2)

    d_1 = datetime.date.today()
    d_2 = datetime.date.today()  + datetime.timedelta(days=1)
    print (d_1)
    print (d_2)
    print ('d_1 > d_2 :', d_1 > d_2)


def combine_date_and_time():
    print ('Now  :', datetime.datetime.now())
    print ('Today:', datetime.datetime.today())
    
    d = datetime.datetime.now()
    print ('datetime Year:', getattr(d, 'year'))
    print ('datetime Hour:', getattr(d, 'hour'))

    t = datetime.time(1, 2, 3)
    d = datetime.date.today()

    dt = datetime.datetime.combine(d, t)
    print (dt)

def format_and_parse():
    dt = datetime.datetime.now()
    print (dt)

    dt_format = '%Y-%m-%d %H:%M:%S'
    dt_str = dt.strftime(dt_format)
    print (dt_str)

    dt_new = datetime.datetime.strptime(dt_str, dt_format)
    print (dt_new.strftime(dt_format))

    print ('{:%Y-%m-%d}'.format(dt))



def datetime_func():
    """
    Args:
    Returns:
    Raises:
    """
    format_and_parse()
    combine_date_and_time()
    date_compare_study()
    date_arithmetic_study()
    timedelta_study()
    date_study()
    time_study()

if __name__ == "__main__":
    datetime_func()
