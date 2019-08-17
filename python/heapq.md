dt: 2019-08-17

heapq模块学习记录
###1. heappush
Args: list、添加的元素

该list本身已经是最小堆，向list结尾添加元素，调用_sifedown方法维持最小堆的格式；

#### _siftdown
这个down是针对父节点而言的，如果插入的新元素小于父节点，那么意味着父节点需要向下移动

###2. heappop
Args: list

list已经是最小堆

该函数需要做两件事，返回最小值、并调整结构

list的下标为0的元素就是需要返回的元素

将list的最后一个元素pop，并将其放入到list的index为0的位置

调用_siftup方法
#### _siftup
将index为0的元素设计为要新添加的元素

将index为0的位置空出来，将左右子节点中较小的上移，直到结束，找到新元素添加的位置

将新元素添加的到该位置

调用 _siftdown方法

### 3. heappushpop
Args: list, item
功能是：先将item加入到，再将最小的pop，并返回

如果list是空或者item比最小的元素还要小，直接返回item

否则将item放到list的index为0的位置

与heappop一样，调用_siftup方法

### 4. heapify
Args: list
将一个list转化成最小堆

从 n // 2开始 逆序调整， 执行 _siftup方法


### 5. nlargest
Args: n, list

获取list中n个最大的元素

1. 截取list的 n 个元素，调用 heapify 生成最小堆
2. 遍历list，执行heappushpop 操作
3. 逆序返回最小堆

### 对偶问题
|编号|最小堆|最大堆|
|:--|:--:|:--:|
|1| heappush|
|2| heappop|
|3| heappushpop| \_heappushpop_max|
|4| heapify|\_heapify_max|
|5| nlargest| nsmallest| 
|6| \_siftdown|\_siftdown_max|
|7| _siftup| \_siftup_max|


### TODO

- [ ] merge
      多个有序的list，进行合并；使用了迭代器
      
- [ ] nlargest、nsmallest
      涉及到指定key
      
- [ ] itertools 模块
      涉及到islice, count, imap, izip, tee, chain




