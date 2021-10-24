# 1、什么是名称空间
"""
名称空间是存放名字与值绑定关系的地方      {"name": 0x000001B7C21E6438}

要取到值必须通过名字才能找，而名字又在名称空间中存放着，所以我们在取值时首先是去名称空间中名字
找到了名字自然就拿到值的内存地址。。。。
# eg:
name = 10
print(name) # 过程：先到名称空间找到name，然后通过name取地址
"""

# 2、名称空间分为三种：
"""
1）内置名称空间:存放的python解释器自带的名字
    生命周期：在解释器启动时产生，在解释器关闭时回收

2）全局名称空间：除了内置的与局部的之外名字都属于全局名称空间
    生命周期：在程序文件执行时就立刻产生，在程序执行完毕后就回收

# eg1:
# 其中：x，y，foo，z都是全局名称空间中的名字
x = 1
y = 2

def foo():
    x = 1
    y = 2


foo()

if y > x:
    z = 3

3）局部名称空间:存放的是函数内部定义的名字
    生命周期：在调用函数时临时生效，在函数结束后立刻回收

    def sum(x, y):
        sum = x + y
        return sum

    加载顺序：内置名称空间 ==> 全局名称空间 ==> 局部名称空间
        加载名称空间的目的是为了将名字与值的绑定关系存放起来
        而存的目的是为了取，也就是说，当我们在查找名字时，必然是在三者之一找到

    查找顺序：局部名称空间 ==> 全局名称空间 ==> 内置名称空间
        基于当前所在的位置往后查找

# eg1:
length = 100
print(length)   # 站在全局查找


def foo():
    print(length)   # 站在全局查找


def foo2():
    count = 200
    print(count)    # 站在局部查找


foo()
foo2()

# eg2:
x = 100
y = 200


# 强调：函数的形参名属于局部名称空间
def foo(x, y):
    print(x, y)


foo(1, 2)

x = 2222


def f1():
    # x = 1

    def f2():
        # x = 2
        print('from f2', x)
    f2()


x = 1111
f1()

"""

# 3、作用域
"""
域指的是范围，作用域指的是作用范围
    分为：
        全局作用范围：包含内置名称空间与全局名称空间中的名字
            特点：全局有效，全局存活
        局部作用范围：包含的局部名称空间的名字
            特点：局部有效，临时存活
# eg1：
x = 1


def f1():
    def f2():
        def f3():
            x = 3
            print(x)
        f3()
    f2()


f1()


def foo():
    print(x)


foo()


# 了解：globals与locals
x = 1111


def foo():
    y = 2
    print(locals())


# print(globals())    # 返回的是全局作用域中的名字
# print(dir(globals()['__builtins__']))   # 返回的是全局作用域中的名字
# print(locals())
# print(locals() is globals())
foo()

"""

# 如何打破函数层级带来的访问限制，让我能够在任意位置都可以访问到一个内部函数
# 基于函数对象的概念将一个内部函数返回到全局使用，从而打破了函数的层级限制


# （******）
# 函数的作用域关系是在函数定义阶段就已经固定死的，与函数的调用位置无关，
# 即在调用函数时一定要跑到定义函数的位置寻找作用域关系
"""
x = 1111


def outer():
    x = 3333

    def inner():
        print('from inner', x)
        # print(locals())
        # x=4444
    # locals()['inner']()     # == inner()
    return inner


# outer()
f = outer()     # f = 指向outer.locals.inner
f()


def foo():
    x = 222
    f()


foo()
x = 4444
"""

# global :在局部声明名字是来自于全局的
# eg1:
"""
x = 1


def func():
    global x
    x = 2


func()
print(x)
"""

# eg2:
"""
x = []


def func():
    x.append(1)


func()
print(x)
"""

# nonlocal : 声明变量是来自于当前层外层的（必须是在函数内的）
# eg1：
"""
x = 222


def f1():
    x = 111

    def f2():
        global x
        x = 0

    f2()    # 全局：x = 0 局部：x = 111
    print('f1---》', x)  # 基于当前的顺序往后查找 局部名称空间 ==> 全局名称空间 ==> 内置名称空间


f1()
print(x)    # 只能找到全局和内置，故：x = 0
"""

# eg2:
"""
x = 222


def f1():
    x = 111

    def f2():
        nonlocal x
        x = 0

    f2()    # 全局：x = 222 局部：x = 0
    print('f1==>', x)  # x = 0


f1()
print('global==>', x)   # x = 222
"""