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
内置的dict，使用setdefault方法

