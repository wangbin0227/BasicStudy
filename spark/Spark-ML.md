MLlib是Spark的机器学习（ML）库，目标是使实际的机器学习变得可扩展和容易，提供了以下工具：
ML算法：

- 常见的学习算法，如分类、回归、聚类和协同过滤。
- 特征工具：特征提取、转换、降维和选择
- Pipeline：构建、评估和调优的工具
- 持久化：保存和加载算法、模型和Pipeline
- 实用性工具：线性代数、统计、数据处理等


协同过滤


ALS将评分矩阵R分解为两个低阶矩阵X和Y的乘积，通常这些近似值称为“因子”矩阵。通用的分解方法是迭代，在每一轮迭代过程中，一个因子矩阵保持不变，而另一个因子矩阵则使用最小二乘法求解。新求解的因子矩阵在求解另一个因子矩阵时保持不变。

ALS的分解算法是通过分块实现的，将两组因子（通常是user和item）分组为块，在每一轮迭代过程中，向item块发送user向量的副本来减少通信：只需要发送item块需要的用户特征向量。这是通过预计算评分矩阵R的信息来实现的：user的“外链”（贡献给哪些item块）和item的“内链”信息（依赖于哪些用户块）。这就允许我们只在user块和item块之间发送一组特征向量，并让item块根据这些信息查找用户评级并更新产品。

对于隐式偏好数据，算法基于AAA，适用于该分块方法。

本质上不是求解评分矩阵R的低阶近似值，而是求解偏好矩阵P的近似值，其中P的元素 在r>0时为1，否则为0。该值作为“信心”值，与用户偏好强度相关，而不是对item的显式评分。


pyspark.ml.recommendation

```
ALS(rank=10, maxIter=10, regParam=0.1, numUserBlocks=10, 
numItemBlocks=10, implicitPrefs=False, alpha=1.0, 
userCol='user', itemCol='item', seed=None, 
ratingCol='rating', nonnegative=False, checkpointInterval=10, 
intermediateStorageLevel='MEMORY_AND_DISK', 
finalStorageLevel='MEMORY_AND_DISK', coldStartStrategy='nan', 
blockSize=4096)
```

### 参数描述

|编号|参数名|描述|get|set|备注|
|:--:|:--:|:--:|:--:|:--:|:--|
|1|rank|分解的阶数|getRank()|setRank(value)|rank = Param(parent='undefined', name='rank', doc='rank of the factorization')|
|2|maxIter|最大迭代轮次|getMaxIter()|setMaxIter(value)|maxIter = Param(parent='undefined', name='maxIter', doc='max number of iterations (>= 0).')|
|3|regParam|正则化参数|getRegParam()|setRegParam(value)|regParam = Param(parent='undefined', name='regParam', doc='regularization parameter (>= 0).')|
|4|numUserBlocks|user 块的数量|getNumUserBlocks()|setNumUserBlocks(value)|numUserBlocks = Param(parent='undefined', name='numUserBlocks', doc='number of user blocks')|
|5|numItemBlocks|item 块的数量|getNumItemBlocks()|setNumItemBlocks(value)|numItemBlocks = Param(parent='undefined', name='numItemBlocks', doc='number of item blocks')|
|6|implicitPrefs|是否使用隐式偏好|getImplicitPrefs()|setImplicitPrefs(value)|implicitPrefs = Param(parent='undefined', name='implicitPrefs', doc='whether to use implicit preference')|
|7|alpha|alpha for implicit preference|getAlpha()|setAlpha(value)|alpha = Param(parent='undefined', name='alpha', doc='alpha for implicit preference')|
|8|userCol|user的列名|getUserCol()|setUserCol(value)|userCol = Param(parent='undefined', name='userCol', doc='column name for user ids. Ids must be within the integer value range.')
|9|itemCol|item的列名|getItemCol()|setItemCol(value)|itemCol = Param(parent='undefined', name='itemCol', doc='column name for item ids. Ids must be within the integer value range.')|
|10|seed|随机种子|getSeed()|setSeed(value)|seed = Param(parent='undefined', name='seed', doc='random seed.')|
|11|ratingCol|评分的列名|getRatingCol()|setRatingCol(value)|ratingCol = Param(parent='undefined', name='ratingCol', doc='column name for ratings')|
|12|nonnegative|whether to use nonnegative constraint for least squares|getNonnegative()|setNonnegative(value)|nonnegative = Param(parent='undefined', name='nonnegative', doc='whether to use nonnegative constraint for least squares')|
|13|checkpointInterval|checkpoint interval|getCheckpointInterval()|setCheckpointInterval(value)|checkpointInterval = Param(parent='undefined', name='checkpointInterval', doc='set checkpoint interval (>= 1) or disable checkpoint (-1). E.g. 10 means that the cache will get checkpointed every 10 iterations. Note: this setting will be ignored if the checkpoint directory is not set in the SparkContext.')|
|14|intermediateStorageLevel|StorageLevel for intermediate datasets|getIntermediateStorageLevel()|setIntermediateStorageLevel(value)|intermediateStorageLevel = Param(parent='undefined', name='intermediateStorageLevel', doc="StorageLevel for intermediate datasets. Cannot be 'NONE'.")|
|15|finalStorageLevel|StorageLevel for ALS model factors.|getFinalStorageLevel()|setFinalStorageLevel(value)|finalStorageLevel = Param(parent='undefined', name='finalStorageLevel', doc='StorageLevel for ALS model factors.')|
|16|coldStartStrategy|冷启动策略，取值有nan、drop|getColdStartStrategy()|setColdStartStrategy(value)|coldStartStrategy = Param(parent='undefined', name='coldStartStrategy', doc="strategy for dealing with unknown or new users/items at prediction time. This may be useful in cross-validation or production scenarios, for handling user/item ids the model has not seen in the training data. Supported values: 'nan', 'drop'.")|
|17|blockSize|分块大小|getBlockSize()|setBlockSize(value)|blockSize = Param(parent='undefined', name='blockSize', doc='block size for stacking input data in matrices. Data is stacked within partitions. If block size is more than remaining data in a partition then it is adjusted to the size of this data.')|


### 其他get/set方法

|编号|说明|get|set|
|:--|:--|:--|:--|
|1|预测列名|getPredictionCol()|setPredictionCol(value)|
|2|基于参数名|getParam(paramName)、getOrDefault(param)|set(param, value)|
|3|所有参数|property params|setParams(self, rank=10, maxIter=10, regParam=0.1, numUserBlocks=10, numItemBlocks=10, implicitPrefs=False, alpha=1.0, userCol="user", itemCol="item", seed=None, ratingCol="rating", nonnegative=False, checkpointInterval=10, intermediateStorageLevel="MEMORY_AND_DISK", finalStorageLevel="MEMORY_AND_DISK", coldStartStrategy="nan", blockSize=4096)|
|4|参数判定|hasDefault(param)、hasParam(paramName)、isDefined(param)、isSet(param)|
|5|清除参数|clear(param)|
|6|参数详情|explainParam(param)、explainParams()、extractParamMap(extra=None)|


### 模型训练

1. fit(dataset, params=None)

Fits a model to the input dataset with optional parameters.

Parameters
dataset – input dataset, which is an instance of pyspark.sql.DataFrame

params – an optional param map that overrides embedded params. If a list/tuple of param maps is given, this calls fit on each param map and returns a list of models.

Returns
fitted model(s)


2. fitMultiple(dataset, paramMaps)
Fits a model to the input dataset for each param map in paramMaps.

Parameters
dataset – input dataset, which is an instance of pyspark.sql.DataFrame.

paramMaps – A Sequence of param maps.

Returns
A thread safe iterable which contains one model for each param map. Each call to next(modelIterator) will return (index, model) where model was fit using paramMaps[index]. index values may not be sequential.


## ALSModel 类

### 类方法
|编号|方法|描述|
|:--|:--|:--|
|1|load(path)|从输入路径中加载模型，read().load(path)的简写|

### 实例方法
|编号|方法|描述|
|:--|:--|:--|
|1|recommendForAllItems(numUsers)|
|2|recommendForAllUsers(numItems)|
|3|recommendForItemSubset(dataset, numUsers)|
|4|recommendForUserSubset(dataset, numItems)|
|5|save(path)|
|6|transform(dataset, params=None)|


### 属性
|编号|name|描述|
|:--|:--|:--|
|1| itemFactors|
|2| userFactors|
