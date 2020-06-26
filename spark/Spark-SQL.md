Spark SQL 是一个用于结构化数据处理的Spark模块。与基本的Spark RDD API不同，Spark SQL提供的接口为Spark提供了正在执行的计算和数据更多的结构信息，在内部，Spark SQL会使用这些额外的信息进行优化。

Spark SQL的交互方式：SQL 和 Dataset API

Spark SQL屏蔽了API和语言的差异，使用了相同的执行引擎。

Dataset：表示数据的分布式集合，在Spark 1.6版本新增，集合了RDD和Spark SQL的优化的执行引擎的优点。但是Python并不支持该接口。

DataFrame: 组织成命名列的Dataset，在概念上等同于关系数据库的表。DataFrame可以从大量的数据源中构建，如：结构化文件、Hive表、外部数据库以及RDD。


Spark SQL 所有功能的入口是SparkSession类

在Spark 2.0中，SparkSession对Hive提供了内置的支持。

在Python中，可以属性或者索引访问DataFrame的列：推荐使用索引。

除了简单的列引用和表达式之外，DataFrame还有丰富的函数库：包括字符串操作、日期算术、常见的数学操作等等。


## Data Sources

Spark SQl支持通过DataFrame接口，对各种数据源进行操作。

Save操作可以指定SaveMode：标记如何处理已用的数据（如果存在）。
这些存储模式没有使用锁，也不是原子操作。当模式为Overwrite时，在写入新数据之前，会将原有数据删除


|Save 模式| 说明|
|:--|:--|
|error（errorifexists)|当数据存在时，直接报错|
|append| 当数据存在时，直接追加|
|overwrite|当数据存在时，直接覆盖|
|ignore|直接忽略，相当于SQL中的：CREATE TABLE IF NOT EXISTS |

对于基于文件的数据源，通过path选项指定自定义表的路径，如df.write.option("path", "/AAA/BBB").saveAsTable("table_name")，当删除表时，不会删除该路径下的数据。如果未指定自定义表路径，Spark会将数据写入仓库目录下的默认表路径，删除表时，该默认的表路径也将被删除。


基于文件的数据源，如：parquet、orc、avro、json、csv、text等，可以设置通用配置
|通用配置| 说明|
|:--|:--|
|spark.sql.files.ignoreCorruptFiles|忽略损坏的文件，继续执行|
| spark.sql.files.ignoreMissingFiles|忽略丢失的文件，继续执行|
|pathGlobFilter| 文件匹配|
| recursiveFileLookup|递归查询文件|


Parquet是许多数据处理系统都支持的列式存储格式。Spark SQL支持Parquet文件的读写，出于兼容的考虑，读取Parquet文件时，所有列都自动转为nullable。

Hive中常用优化方法是表分区，在分区表中，数据通常存储在不同的目录中，分区列的值编码在分区路径中。Spark SQL内置的基于文件数据源能够自动发现和推断分区信息。


分区列的数据类型是自动推断的，支持：数字、日期、时间戳、字符串类型。自动推断是默认开启的，如果需要关闭，将spark.sql.sources.partitionColumnTypeInference.enabled设置为false，关闭自动推断后，所有分区列的类型均为字符串。


