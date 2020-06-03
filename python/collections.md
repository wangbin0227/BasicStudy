collections模块包含了除了内置类型list、dict、tuple之外的容器类型。


[toc]

### Counter
Counter是用来记录相等值出现次数的容器，与其他语言的bag或者multiset数据结构的算法是一致的。
#### 初始化
Counter支持三种方式的初始化：

1. 列表序列
2. dict，包含键值和计数
3. 关键字参数

```
def counter_container():
    cur_counter = collections.Counter
    print (cur_counter(['a', 'b', 'c', 'd', 'a', 'a', 'b']))
    print (cur_counter({'a':3, 'b': 2, 'c': 1, 'd': 1}))
    print (cur_counter(a=3, b=2, c=1, d=1))
    
```
可以创建空的Counter，使用update方法进行更新：计数值根据新的数据增加，而不是替换。

```
	cur_counter_demo = collections.Counter()
	cur_counter_demo.update('abcda')
	print (cur_counter_demo)
	cur_counter_demo.update({'a':3, 'd':4})
	print (cur_counter_demo)
```

#### 数据访问

Counter创建后，可以通过dict的API进行访问

```
def counter_access():
    cur_counter_demo = collections.Counter(['a', 'b', 'c', 'd', 'a', 'a', 'b'])
    for letter in 'abcdef':
        print ('{} : {}'.format(letter, cur_counter_demo[letter]))

    cur_counter_demo['z'] = 0
    print (cur_counter_demo)
    print (list(cur_counter_demo.elements()))


    print (cur_counter_demo.most_common(2))
```

Counter的elements方法，返回一个迭代器，包含所有的元素（计数<=0的元素除外）

most_common方法，返回元素为tuple的list，包含key和count

#### 算术计算
对于聚合结果，Counter实例支持算术操作：操作结果中，计数<=0的值，会被丢弃。

```
def counter_arith():
    counter_1 = collections.Counter(['a', 'b', 'a', 'c', 'b', 'a'])
    counter_2 = collections.Counter({'a':2, 'c':2, 'd':1})
    print ('counter_1: ', counter_1)
    print ('counter_2: ', counter_2)

    print ('add: ', counter_1 + counter_2 )
    print ('sub: ', counter_1 - counter_2)
    print ('&: ', counter_1 & counter_2)
    print ('|: ', counter_1 | counter_2)
```
对于&操作：选择两者间最小的整数。对于|或操作：选择两者最大值

### defaultdict
内置的dict，使用setdefault方法设置当key不存在时，对应的默认值。对于defaultdict，容器在初始化的时候，预先指定了默认值。

```
def defaultdict_module():
    def _default_factory(value):
        return lambda : value
    d = collections.defaultdict(_default_factory('default_value'))
    print (d['unknown'])

    d = collections.defaultdict(list)
    print (d['test'])

    d = collections.defaultdict(int)
    print (d['test'])
```

### namedtuple

内置的tuple使用下标来访问数据，使得tuple成为便于简单使用的容器。然而，当tuple有很多字段或者构造位置远离使用位置时，确定该使用哪个下标会很困难。namedtuple为每个成员分配了名称和数字索引。

#### 定义

namedtuple没有创建实例字典，因此具有和常规tuple一样的内存效率。每种namedtuple都由自己的类表示，该类使用namedtuple()工厂函数创建：参数是类的名称和包含字段名称的字符串。

```
def namedtuple_module():
    Person = collections.namedtuple('Person', 'name age')
    p = Person(name='Bob',age=21)
    print (p)
    print (p.name)
    print (p[1])
```
上述例子可以使用.属性名读取，或者类似于内置tuple使用下标访问。
和内置tuple一样，namedtuple是不可以修改的，如果尝试修改，会提示AttributeError错误。

#### 无效字段名
字段名是无效的，如果重复或者和Python关键字冲突，但是可以将rename选项设置为True，重命名无效字段。

```
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
    
```

#### 特殊属性
namedtuple为处理子类和实例提供了一些有用的属性和方法，所有这些内置的属性都是以下划线(_)作为前缀，Python的惯例是下划线表示私有属性，但是对于namedtuple使用下划线前缀是为了防止名称与用户提供的属性名称冲突。

|内置属性|描述|
|:--:|:--:|
|_fields|定义namedtuple使用的字段名称|
|_asdict|转换为OrderedDict实例|
|_replace|创建一个新的namedtuple实例，替换原来的某些值|

### OrderedDict
OrderedDict是dict的子类 ，存储了元素的添加顺序。python3.6之前，内置的dict是不跟踪添加顺序的，python3.6之后，内置的dict跟踪了添加顺序，但是不应该依赖这个。

```
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
```

内置的dict：内容相同的即为相等；但是对OrderedDict，是否相等需要考虑添加顺序。
OrderedDict可以更改元素的顺序：使用move_to_end方法

```
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
```

### ChainMap
ChainMap类管理一系列的字典，按照给定的顺序搜索字典，查找给定key的value。
#### 数据访问
ChainMap支持和内置dict一样访问。对于子dict，按照构造器传入顺序进行访问，因此，多个相同的key，取最先有值的。

```
def chain_map_module():
    a = {'a': 1, 'c': 3}
    b = {'b': 2, 'c': 4}
    m = collections.ChainMap(a,b)
    print (m)
    for k, v in m.items():
        print (k, v)
    print (m['c'])
```
#### 重新排序
ChainMap的maps属性是一个list，存储了dict的查询顺序。这个list是可变的，可以添加新的dict或者更改现有dict的顺序

```
def chain_map_module():
    a = {'a': 1, 'c': 3}
    b = {'b': 2, 'c': 4}
    m = collections.ChainMap(a,b)
    print (m)
    print (m['c'])
    
    print (m.maps)
    m.maps = list(reversed(m.maps))
    print (m['c'])
    
    m.maps.append({'e': 5})
    print (m.maps)
    print (m['e'])
```

#### 更新
ChainMap没有缓存dict的内容，因此当dict值改变后，同样会影响ChainMap的取值。

```
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
```
同样，通过ChainMap修改，也会影响到原始dict的值；
ChainMap提供了一个很方面的方法：new_child()，创建一个新的实例：新增了一个额外的dict，放到最前面，这样可以避免修改现有的底层数据结构。
这种堆叠行为使得使用ChainMap作为模板或应用程序上下文变得非常方便。具体来说，在一次迭代中添加或更新值很容易，然后在下一次迭代中放弃更改。

### deque
deque支持在队列的双端端添加和删除元素，常用的stack和queue是deque的退化形式：输入和输出被限制在单端。
deque作为序列容器的一种，支持与list相同的一些操作，比如：使用下标访问元素、长度获取、从队列中间删除元素等

#### 构建
deque可以从双端构建，在Python中使用left和right进行构建。

```
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
```
extendleft方法的功能是：对输入进行迭代，对每一项执行appendleft等价的操作，因此最终结果相当于输入的逆序。

#### 消费
deque可以进行双端消费；deque是线程安全的，支持多线程同时访问。

```
    d = collections.deque(range(5))
    print (d)
    print (d.pop())
    print (d.popleft())
```

#### 限制队列大小
deque实例可以配置最大长度，当队列达到指定长度后，在添加新元素时，会丢弃原有的元素：对于在长度不确定的流中查找最后n个项非常有用。

```
    d = collections.deque(maxlen=3)
    d2 = collections.deque(maxlen=3)
    for i in range(5):
        print ('---- {} ---- '.format(i))
        d.append(i)
        d2.appendleft(i)
        print (d)
        print (d2)
```



