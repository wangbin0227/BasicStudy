shuffle影响了Spark作业的性能，主要是：磁盘IO、序列化、网路传输

在Spark源码中，ShuffleManager负责管理shuffle的执行、计算和处理

### HashShuffleManager
HashShuffleManager的问题是：大量的中间磁盘文件。

未优化，文件数量 = map task数量 * reduce task 数量

优化后：spark.shuffle.consolidateFiles 

ShuffleFileGroup的概念：每个cpu core 会创建一个

文件数量 = executor num * cpu cores * reduce task数量

### SortShuffleManager

文件数量 = map task数量


普通运行机制


bypass机制

触发条件：

- map task数量 < spark.shuffle.sort.bypassMergeThreshold
- 非聚合类shuffle算子


|参数| 作用|
|:--|:--|
|spark.shuffle.file.buffer|设置shuffle write 的BufferedOutputStream的buffer大小，数据在写入磁盘前，会先写入到buffer中|



### 官方文档
[shuffle](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations)

spark的某些操作会触发shuffle事件，shuffle是spark用于重新分发数据的机制。这涉及到跨机器操作，因此shuffle是复杂而昂贵的操作







