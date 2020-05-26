目标：datetime模块包含用于进行日期和时间解析、格式化和运算的函数与类

### 时间
时间值可以通过time类表示，time实例包含小时、分钟、秒、毫秒属性，同时也包含时区信息。
time实例只保存时间取值，和日期没有关系。time的精度是微妙。

```
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
```

### 日期
日历日期值可以通过date类表示，date实例包含年、月、日属性。使用类方法today()可以很容易的创建当前日期。下述展示创建日期的几种方式

- 使用固定值
- 使用时间戳
- 使用replace方法

```
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
```


### timedeltas
两个datetime对象或者datetime对象和timedelta通过算术操作，可以得到其他日期。两个date相减可以得到timedelta。timedelta内部以天、秒、微秒为单位存储。

```
def timedelta_study():
    print ('hours: ', datetime.timedelta(hours=10))
    print ('days: ', datetime.timedelta(days=1, seconds=100))

    delta = datetime.timedelta(days=1, seconds=100)
    print ('total seconds: ', delta.total_seconds())
```

### 日期算术
日期支持标准的算术运算符，下述例子中展示了使用timedelta产生新的日期以及两个日期相减得到timedelta。

```
def date_arithmetic_study():

    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)

    yesterday = today - one_day
    tommorow = today + one_day

    print ('today: ', today)
    print ('yesterday: ', yesterday)
    print ('tommorow: ', tommorow)

    print ('tommorow - yesterday: ', tommorow - yesterday)
```

### 日期比较
date和time实例支持标准的比较运算符，可以确定那个日期更早或更晚

```
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
```

### 日期和时间合并
datetime类合并了date和time组件，与date一样，有几个方便的类方法创建datetime实例。

```
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
```

### 日期格式化与解析
datetime默认字符串表示使用的是ISO-8601格式，
strftime：将datetime转换成指定格式
strptime：将指定格式的字符串转换成datetime对象

```
def format_and_parse():
    dt = datetime.datetime.now()
    print (dt)

    dt_format = '%Y-%m-%d %H:%M:%S'
    dt_str = dt.strftime(dt_format)
    print (dt_str)

    dt_new = datetime.datetime.strptime(dt_str, dt_format)
    print (dt_new.strftime(dt_format))

    print ('{:%Y-%m-%d}'.format(dt))
```

|符号|描述|
|:---:|:----:|
|%Y|完整年份，带世纪|
|%m|月份|
|%d|日(零填充)|
|%H|小时（24时制）|
|%M|分钟|
|%S|秒|
|%w|周几|
|%W|该年的第几周|
|%j|该年的第几天|




