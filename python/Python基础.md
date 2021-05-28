Python的数据结构：容器(container)、可迭代对象(iterable)、迭代器(iterator)、生成器(generator)、列表/集合/字典推导式(list,set,dict comprehension)

可迭代的对象必须实现__iter__方法，但不能实现__next__方法。

迭代器应该一直可以迭代，迭代器的__iter__方法应该返回自身。

虽然可迭代对象和迭代器都有__iter__方法，但是两者的功能不一样，可迭代对象的__iter__用于实例化一个迭代器对象，而迭代器中的__iter__用于返回迭代器本身，与__next__共同完成迭代器的迭代作用。​


迭代器可以迭代，但是可迭代的对象不是迭代器。


### 取整操作

1. 向上取整：math.ceil()
2. 向下取整：math.floor()
3. 四舍五入取整：round，需要注意的是小数末尾为5的情况（存储为49999）
4. 向0取整：int()
5. 取模操作：//，处理结果与math.floor一致


### 内置函数

| 一级分类 | 二级分类|相关函数 | 说明 |
| :--:|:--:|:--:|:--|
|数字相关|数据类型| bool、int、float、complex| 布尔、整型、浮点、复数|
|数字相关|进制转换 | bin、oct、hex||
|数字相关|数学运算| abs、pow、divmod、round、min、max、sum|
|数据结构| 容器创建 | tuple、list、dict、set、frozenset | frozenset创建一个不可变的集合 |
|数据结构| 序列操作 | map、filter、all、any、reversed、sorted、zip|
|迭代器| 迭代器相关| range、iter、next||


