Python中使用iterators编程时，通常需要为简单表达式创建小函数。有时候可以通过lambda表达式实现，但是对于某些操作并不需要创建新的函数。operator模块定义了与内置运算相对应的函数，如算术操作、比较操作以及和标准API相对应的操作。

### 逻辑操作
这些函数用于判定给定的值是否布尔相等，对其取反创建相反的布尔值以及比较操作判断是否相等

```
def logical_operations():
    a = -1
    b = 5
    print ('a =', a)
    print ('b =', b)
    print ()

    print ('not_(a)     :', not_(a))
    print ('truth(a)    :', truth(a))
    print ('is_(a, b)   :', is_(a, b))
    print ('is_not(a, b):', is_not(a, b))   
```

### 比较操作
支持丰富的比较运算符

```
def comparison_operations():
    a = 1
    b = 5.0

    print ('a = ', a)
    print ('b = ', b)

    for func in (lt, le, eq, ne, gt, ge):
        print ('{}(a, b): {}'.format(func.__name__, func(a, b)))
        
```

### 算术操作
支持数值间的算术运算符：绝对值、加减乘除操作、位运算(与、或、非、异或、左移、右移)

```
def arithmetic_operations():
    a = -1
    b = 5.0
    c = 2
    d = 6

    print ("Positive/Negative")
    print ('abs(a):', abs(a))
    print ('neg(b):', neg(b))
    print ('pos(c):', pos(c))

    print ("\nArithmetic")
    print ("add(a, b)      :", add(a, b))
    print ("sub(b, a)      :", sub(b, a))
    print ("mul(a, b)      :", mul(a, b))
    print ("floordiv(a, b) :", floordiv(a, b))
    print ("truediv(a, b)  :", truediv(a, b))
    print ("floordiv(d, c) :", floordiv(d, c))
    print ("truediv(d, c)  :", truediv(d, c))
    print ("mod(a, b)      :", mod(a, b))
    print ("pow(c, d)      :", pow(c, d))

    print ("\nBitwise")
    print ("and_(c, d)", and_(c, d))
    print ("invert(c)", invert(c))
    print ("lshift(c, d)", lshift(c, d))
    print ("or_(c, d)", or_(c, d))
    print ("rshift(d, c)", rshift(d, c))
    print ("xor(c, d)", xor(c, d))
```
floordiv 整数相除；truediv 浮点数相除

### 序列操作

序列运算符可以分为四类：序列建立、序列项搜索、序列访问、序列搜索

```
def sequence_operations():
    a = [1, 2, 3]
    b = ['a', 'b', 'c', 'd']
    print ("Constructive")
    print ("concat(a, b): ", concat(a, b))

    print ("\nSearching")
    print ("contains(a, 1) :", contains(a, 1))
    print ("countOf(b, 'c'):", countOf(b, "c"))
    print ("countOf(b, 'd'):", countOf(b, "d"))
    print ("indexOf(a, 1)  :", indexOf(a, 1))


    print ("\nAccess Items")
    print ("getitem(b, 1) :", getitem(b, 1))
    print ("getitem(b, slice(1, 3)) :", getitem(b, slice(1, 3)))
    print ("setitem(b, 1, 'd') :", end = ' ')
    setitem(b, 1, "d")
    print (b)

    print ("\nDestructive")
    print (" delitem(b, 1) :", end=" ")
    delitem(b, 1)
    print (b)
```
setitem 和 delitem都是原地修改序列，没有返回值

### 原地操作

除了标准运算符之外，许多类型的对象都支持通过特殊运算符（如 +=）进行“原地”修改。同样有等价于就地修改的函数

```
def inplace_operations():
     a = -1
     b = 5.0
     c = [1, 2, 3]
     d = ['a', 'b', 'c']

     a = iadd(a, b)
     print ('a = iadd(a, b) =>', a)

     c = iconcat(c, d)
     print ('c = iconcat(c, d) =>', c)
```

### Getters操作
operator模块中不常用的特性之一是Getters概念。运行时，构造的可调用对象，用于从序列中检索对象或者内容属性；当使用迭代器或者生成器序列时，Getters特别有用：比lambda或Python函数花费更小的开销。

```
class MyObj:
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

def getters_operations():

    ### attrgetter
    l = [MyObj(i) for i in range(5)]
    print ('objects :', l)

    g = attrgetter('arg')
    vals = [g(i) for i in l]
    print ('arg values:', vals)

    l.reverse()
    print (l)
    print ('sorted :', sorted(l, key=g))

    ### itemgetter
    l = [dict(val= -1 * i) for i in range(4)]
    print ('original: ', l)
    g = itemgetter('val')
    vals = [g(i) for i in l]
    print (values)

```

其他：operator模块中的函数(lt等)通过标准Python接口进行操作，因此这些函数可以作用于用户定义的类，与内置类型一致。



