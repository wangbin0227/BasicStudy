FP Tree算法引入了一些数据结构来临时存储数据

FP Tree 数据结构

1. 项头表：记录一项频繁项集出现的次数，按照次数降序排列
2. FP Tree
3. 节点链表：项表头的恨一个元素都是节点链表的头。


项头表建立

1. 扫描数据，对一项频繁集进行计数，根据预先定义的阈值，删除低于阈值的项，生成频繁一项集
2. 第二次扫描数据，对于每条数据，剔除非频繁一项集中的项，并按照支持度降序排列。

FP树建立


[cosine_similarity](https://zh.wikipedia.org/wiki/%E4%BD%99%E5%BC%A6%E7%9B%B8%E4%BC%BC%E6%80%A7)


FP是frequent pattern的简写
第一步 生成频繁项集
第二步 使用后缀树（FP-tree）进行编码
第三步 从FP树中提取频繁项集


spark.ml实现使用了以下超参数

1. minSupport：最小支持度
2. minConfidence：最小置信度
3. numPartitions：分布式执行的并发度


FPGrowthModel提供
1. freqItemsets