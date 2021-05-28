本文内容来源于：[MapReduce之Shuffle过程详述](http://matt33.com/2016/03/02/hadoop-shuffle/)

MapReduce过程

1. Map：数据输入，对数据进行预处理，产出指定格式的中间结果
2. Shuffle: 按照partition、key对中间结果进行排序合并，输出给reduce线程
3. Reduce: 对相同key的数据，进行处理，并将结果写入到HDFS文件

