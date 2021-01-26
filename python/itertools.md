## 无穷迭代器
### count
Args: start, step

生成器

相当于生成无限序列


## 有限迭代器
### islice
Args: iterable, start, stop, step

功能是：针对可迭代对象，返回切片

左闭右开，step是步长

调用range(start, stop, step) 生成迭代器

返回的是生成器

## 组合迭代器

dt: 2020-03-08
###merging and splitting iterators
1. chain
2. chain.from_iterable
3. zip
4. islice
5. tee

### converting inputs
1. map  变量
2. starmap \*变量

### producing new values

itertools 库中的方法
count(): 给出初始值、间隔，就可以无限；默认是0、1
cycle()
repeat()

### Filtering
filter()
filterfalse()
dropwhile()
takewhile()
compress()
 


### Grouping Data
groupby

### combining Inputs
accumulate
product
组合
排列
