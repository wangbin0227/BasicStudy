###type、isinstance
type 不考虑继承、

isinstance 考虑继承

###type动态创建类
Python中一切都是对象，包括类也是对象，类是type的对象，type是其本身的对象

type(类名，父类，方法和变量)

1. 类名：是字符串，和class 规范基本一致

2. 父类：是tuple，可以继承多个类

3. 方法和变量：变量是类变量、方法