Spark的两大抽象：RDD和共享变量

|类|功能|
|:--|:--|
|SparkContext|Spark的主要入口|
|RDD|弹性分布式数据集，Spark的基本抽象|
|Broadcast|task间重复使用的广播变量|
|Accumulator|task间的共享变量，只能增加|
|SparkConf|Spark 配置|
|SparkFiles|jobs的可访问文件|
|StorageLevel|控制缓存级别|
|TaskContext|当前正在运行的task信息|
|RDDBarrier|--|
|BarrierTaskContext|--|
|BarrierTaskInfo|--|


## RDD

### RDD的创建

Spark围绕着弹性分布式数据集（RDD）的概念展开，RDD是Spark的基本抽象，表示不可变的分区数据集，可以并行操作。

创建RDD的方式有两种：一是在driver端，并行化已经存在的集合；二是基于外部存储系统的数据源，如共享文件系统、HDFS、HBase以及任何提供Hadoop InputFormat的数据源。

第一种方式使用SparkContext的parallelize方法，可以指定分区数。

第二种方式常用的是SparkContext的textFile方法，URI方式读取文件。同时支持自定义的Hadoop Input/Output 格式


### RDD 算子
分为两类：

- transformations：基于现有的数据集创建一个新的数据集。
- actions：在数据集上进行计算，并将结果返回到driver端。

transformations操作都是惰性的，不会立即计算。actions操作，才会真正的触发执行。

默认情况下，每个action都会重新执行所有的transformations，但是可以通过cache、persist对中间结果进行持久化。


##### Actions 算子

|Action|在python中实现|备注|
|:--|:--|:--|
|collect()| 基础| 只是在数据结果较少的情况下使用，所有的数据都会放到driver内存中|
|collectAsMap()|['collect']|
|reduce(func)	| ['mapPartitions', 'collect']|
| aggregate| ['mapPartitions', 'reduce']|
| fold(zeroValue, op)| ['mapPartitions', 'collect']|使用给定的关联函数和零值，聚合每个分区中的元素，然后聚合所有分区|
|take(n)| 基础|
|first()|调用take(1)|
| takeOrdered(n, [ordering])|['mapPartitions', 'reduce']|
|top|['mapPartitions', 'reduce']|
| count|['mapPartitions']|mapPartitions后，执行sum()|
| countByValue|['mapPartitions', 'reduce']|mapPartitions使用dict存储，执行reduce操作|
| countByKey|['map', 'countByValue']|map后调用countByValue()|


##### Transformations 算子

该类型的算子种类繁多，进行了如下分类：

- 涉及多个RDD

|算子|在python中实现|备注|
|:--|:--|:--|
|join|['python\_join' -> '\_do\_python\_join']|['mapValues', 'union', 'groupByKey', 'flatMapValues']
|leftOuterJoin|['python\_left\_outer\_join' -> '\_do\_python\_join']|
|rightOuterJoin|['python\_right\_outer\_join' -> '\_do\_python\_join']|
| fullOuterJoin|['python\_full\_outer\_join' -> '\_do\_python\_join']|
| cogroup| ['python_cogroup'] | ['mapValues', 'union', 'groupByKey'] 涉及到两个RDD，基于key，聚合两个rdd的value，每个rdd的value是ResultIterable，组成一个tuple|
| groupWith(other, *others)|['python_cogroup'] | 
| intersection| ['map', 'cogroup', 'filter', 'keys']|两个RDD之间的交集，返回的是RDD|
| subtract|['map', 'subtractByKey']|
| subtractByKey| ['cogroup', 'filter', 'flatMapValues']|

调用python_cogroup(rdds, numPartitions)

1. 将每个rdd按顺序编号，并将编号与value组成tuple
2. union多个rdd
3. 对rdd使用groupByKey，并对结果进行格式化

            
- 涉及一个RDD的Aggre操作

|算子|在python中实现|备注|
|:--|:--|:--|
| combineByKey| 基础|原理如下文|
| reduceByKey|['combineByKey']|
| aggregateByKey|['combineByKey']|
| foldByKey|['combineByKey']|
| distinct|['map', 'reduceByKey']|
| groupByKey|['mapPartitions', 'partitionBy', 'mapValues']|

由于combineByKey()会遍历分区中的所有元素，因此每个元素的键要么还没有遇到过，要么就和之前的某个元素的键相同。

1. 如果这是一个新的元素，combineByKey()会使用一个叫作createCombiner()的函数来创建那个键对应的累加器的初始值。需要注意的是，这一过程会在每个分区中第一次出现各个键时发生，而不是在整个RDD中第一次出现一个键时发生。
2. 如果这是一个在处理当前分区之前已经遇到的键，它会使用mergeValue()方法将该键的累加器对应的当前值与这个新的值进行合并。
3. 由于每个分区都是独立处理的，因此对于同一个键可以有多个累加器。如果有两个或者更多的分区都有对应同一个键的累加器，就需要使用用户提供的mergeCombiners()方法将各个分区的结果进行合并。


- 涉及一个RDD的Shuffle操作

|算子|在python中实现|备注|
|:--|:--|:--|
| partitionBy|基础|
| sortByKey | 基础|
| sortBy|['keyBy', 'sortByKey']|
| repartitionAndSortWithinPartitions|['partitionBy', 'mapPartitions']|
|coalesce(numPartitions, shuffle=False)|基础，调整分区数，返回新的RDD|
| repartition|['coalesce']|

- 涉及一个RDD的Map操作

|算子|在python中实现|备注|
|:--|:--|:--|
| mapPartitionsWithIndex| 基础|
| map|['mapPartitionsWithIndex']|
| mapValues|['map']|
| mapPartitions|['mapPartitionsWithIndex']|
|flatMap|['mapPartitionsWithIndex']|
| flatMapValues| ['flatMap']|
| filter|['mapPartitions']|mapPartition，对于迭代器，使用python的filter处理|
| keys|['map']|
| values | ['map']|
| keyBy |['map']|
| lookup|['filter', 'collect']|
| glom|['mapPartitions']|返回RDD，每一个分区的元素合并为一个list，作为一个元素|


- 其他

|算子|在python中实现|备注|
|:--|:--|:--|
| foreach(f)||对RDD的所有元素，应用该函数|
|foreachPartition(f)|||
                                                    

## RDD持久化
Spark的重要功能之一是：可以在内存中进行数据的持久化。涉及到多个action操作时，持久化可以使得计算更快，在算法迭代和快速交互中表现尤其明显。Spark的cache是可以容错的：如果RDD的任何一个分区丢失，可以进行自动重新计算。

持久化涉及到RDD算子：cache、 persist、unpersist

RDD的持久化可以使用不同的级别，StorageLevel对象可以用来描述这些等级。例如：cache使用默认的StorageLevel进行RDD的持久化：MEMORY_ONLY。

每个StorageLevel记录了是否使用磁盘、是否使用内存、是否序列化、是否保存多个副本，详情如下：

```
class pyspark.StorageLevel(useDisk, useMemory, useOffHeap, deserialized, replication=1)
```

|storage levels| 说明|
|:--|:--|
|DISK\_ONLY | StorageLevel(True, False, False, False, 1)|
|DISK\_ONLY\_2 | StorageLevel(True, False, False, False, 2)|
|MEMORY\_ONLY| StorageLevel(False, True, False, False, 1)|
|MEMORY_ONLY_2| StorageLevel(False, True, False, False, 2)| 
|MEMORY\_AND\_DISK| StorageLevel(True, True, False, False, 1)|
|MEMORY\_AND\_DISK\_2| StorageLevel(True, True, False, False, 2)|
|OFF_HEAP| StorageLevel(True, True, True, False, 1)|

Spark的StorageLevel的目的是在内存使用率和CPU效率之间提供不同的权衡。













## 核心关注
1. mapPartitionsWithIndex
2. partitionBy
3. randomSplit
4. collect
5. sortByKey
6. stats
7. take
8. union
9. zip








- max(key=None)

min(key=None)

stdev()

mean()

sum()

variance()

sumApprox(timeout, confidence=0.95)


- randomSplit(weights, seed=None)

sample(withReplacement, fraction, seed=None)
sampleByKey(withReplacement, fractions, seed=None)
sampleStdev()
sampleVariance()
takeSample(withReplacement, num, seed=None)



- zipWithIndex()
zipWithUniqueId()




saveAsHadoopDataset(conf, keyConverter=None, valueConverter=None)

saveAsHadoopFile(path, outputFormatClass, keyClass=None, valueClass=None, keyConverter=None, valueConverter=None, conf=None, compressionCodecClass=None)

saveAsNewAPIHadoopDataset(conf, keyConverter=None, valueConverter=None)

saveAsNewAPIHadoopFile(path, outputFormatClass, keyClass=None, valueClass=None, keyConverter=None, valueConverter=None, conf=None)

saveAsPickleFile(path, batchSize=10)

saveAsSequenceFile(path, compressionCodecClass=None)

saveAsTextFile(path, compressionCodecClass=None)


reduceByKeyLocally(func)

treeAggregate(zeroValue, seqOp, combOp, depth=2)
treeReduce(f, depth=2)

meanApprox(timeout, confidence=0.95)
pipe(command, env=None, checkCode=False)

barrier
cartesian
checkpoint

localCheckpoint()
getCheckpointFile
toLocalIterator()

id()
name()
setName(name)
toDebugString()
isEmpty()
getNumPartitions()

isCheckpointed()
isLocallyCheckpointed()

getStorageLevel()


histogram(buckets)

#### Experimental
countApprox(timeout, confidence=0.95)

countApproxDistinct(relativeSD=0.05)