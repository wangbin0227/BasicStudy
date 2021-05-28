
### 1. 类Serializer

定义了方法：dump\_stream、load\_stream两个核心的未实现方法


### 2. 类BatchedSerializer

继承了类Serializer

实现了 dump\_stream、load\_stream两个方法


### 3. 类FlattenedValuesSerializer

继承了类BatchedSerializer


### 4. 类AutoBatchedSerializer

继承了类BatchedSerializer


### 5. 类CartesianDeserializer

继承了类BatchedSerializer


### 6. 类FramedSerializer 

继承了类Serializer，

实现了 dump\_stream、load\_stream两个方法

新增了方法、dumps、loads 两个核心的未实现方法


### 7. 类PickleSerializer

继承了类FramedSerializer
