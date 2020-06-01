array模块定义了一个序列数据结构，看起来非常像list，只是所有元素必须是相同的原始类型。

支持的类型都是数值或其他固定大小的原始类型，如字节，举例如下：

|Code|Type|最小字节|
|:--:|:--:|:--:|
|f|单精度浮点数| 4字节|
|d|双精度浮点数| 8字节|
|l|有符号长整形| 4字节|
|L|无符号长整形| 4字节|
|i|有符号整型| 2字节|
|I|无符号整型| 2字节|

array使用参数实例化，该参数描述了允许的数据类型，以及需要存储在array中的初始数据序列。

```
def array_initial():
    a = array.array('b', b'abcdefg')
    print (a)

    a = array.array('i', range(3))
    print (a)
    a.extend(range(3))
    print (a)
    print (list(enumerate(a)))
```
如上例子所示：array可以像其他Python的其他序列一样扩展和操作，如切片、迭代、末尾添加元素。

此外，array的内容可以从文件中读取或者写入文件。

```
def array_file():
    import tempfile
    import binascii
    a = array.array('i', range(5))
    print ('A1:', a)
    output = tempfile.NamedTemporaryFile()
    a.tofile(output.file)
    print (output.name)
    output.flush()
    print (output.name)
    with open(output.name, 'rb') as input:
        raw_data = input.read()
        print ('Raw:',binascii.hexlify(raw_data))

        input.seek(0)
        a2 = array.array('i')
        a2.fromfile(input, len(a))
        print ('A2:', a2)
```



