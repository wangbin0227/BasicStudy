time模块提供了多种不同的时钟访问，每一种都有不同的用途，具体如下：

- time()
- monotonic()
- process_time()
- perf_counter()

>上述实现公开了用于处理日期和时间的C库函数，这些库函数与底层C实现相关，因此某些细节是特定于平台的，完整的详细信息，可以参考库文档。

下面将详细介绍
### Clocks比较
clock的实现因平台而异，使用get_clock_info可以当前clock实现的基本信息，包括clock的精度。

```
def clock_basic():
    import textwrap
    available_clocks = [
        ('time', time.time),
        ('monotonic', time.monotonic),
        ('perf_counter', time.perf_counter),
        ('process_time', time.process_time),
    ]

    for clock_name, func in available_clocks:
        print (
            textwrap.dedent('''
            {name}:
                adjustable    :{info.adjustable}
                implementation:{info.implementation}
                monotonic     :{info.monotonic}
                resolution    :{info.resolution}
                current       :{current}'''.format(name=clock_name, info=time.get_clock_info(clock_name), current=func())
            )
        )
```

### time

time模块的核心函数之一是time()，将epoch开始后的秒数作为浮点数返回。
opoch作为时间测量的开始，对于Unix系统而言是：1970年1月1日的0:00，尽管该值是浮点数，实际精度取决于平台。对于时间的存储或者比较，浮点数表示很方便，但是可读性较差，因此对于日志或者打印时间，ctime()方法更有用。

```
def clock_time():
    print (time.time())
    print (time.ctime())
```

### 单调 Clock
用户或者系统服务为了跨机器同步时钟，会修改系统时钟，time()方法查看的是系统时钟，因此多次调用time()方法，可能会产生向前或者向后的值。当使用这些值进行计算或者试图测量连续时间时，会产生意外行为。monotonic()方法，可以避免这种情况，因为只返回向前的值。

```
def clock_monotonic():
    start = time.monotonic()
    time.sleep(0.1)
    end = time.monotonic()
    print (start)
    print (end)
```
monotonic时钟的开始时间为定义，返回值只能用于与其他时钟值的计算。

### 处理器时钟
process_time()返回是处理器时钟时间：表示处理器真实的执行时间，因此当程序没有做任何事情的时候，处理器时钟并不会增加。

```
def processor_clock():
    template = '{} - {:.2f} - {:.2f}'
    print (template.format(time.ctime(), time.time(), time.process_time()))

    for i in range(3, 0, -1):
        time.sleep(i)
        print (template.format(time.ctime(), time.time(), time.process_time()))
```

### 性能计数
高精度的单调时钟对于性能测量非常重要，最佳时钟数据源的确定依赖相关的平台信息，Python在perf_counter中提供了。

```
def perf_counter_clock():
    loop_start = time.perf_counter()

    for i in range(5):
        iter_start = time.perf_counter()
        a = 1
        for i in range(10000):
            a = a + i
        now = time.perf_counter()
        loop_elapsed = now - loop_start
        iter_elapsed = now - iter_start
        print ('{:.6f} {:.6f}'.format(loop_elapsed, iter_elapsed))
```

