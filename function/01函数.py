"""
1、什么是函数
    函数就是具备某一功能的工具

    函数的使用必须遵循先定义、后调用的原则
    事先准备工具的过程即函数的定义
    拿来就用即函数的调用

    函数分为两大类：
        内置的函数
        自定义函数

2、为何要用函数
    1. 程序的组织结构不清晰、可读性差
    2. 日积月累冗余代码过多
    3. 程序的可扩展性极差
"""

# 使用

# 1、定义函数

# 1）语法
'''
def 函数名(参数1,参数2,参数3,...):
    """
    文档注释
    """
    code1
    code2
    code3
    ...
    return 返回值
'''

# 2） 定义函数阶段发生哪些事:只检测语法，不执行代码

'''
def foo():  # foo=函数的内存地址
    print('first')
    print('second')
    print(hello)
    print('third')


foo()
print(foo)
foo = 10
foo()
'''

# 示范一；
'''
def bar():
    print('from bar')


def foo():
    print('from foo')
    bar()


foo()
'''


# 示范二；
'''
# 定义阶段
def foo():
    print('from foo')
    bar()


def bar():
    print('from bar')


# 调用阶段
foo()
'''

# 示范三；
'''
# 定义阶段
def foo():
    print('from foo')
    bar()


# 调用阶段
foo()


def bar():
    print('from bar')
'''

# 3) 定义函数的三种形式

# a. 无参函数

'''
def func1():
    print('hello1')
    print('hello2')
    print('hello3')


func1()
'''


# b. 有参函数
'''
def func2(x, y):
    # x=1
    # y=3
    if x > y:
        print(x)
    else:
        print(y)


func2(1, 3)
func2(2, 3)
func2(2, 4)
'''


# c. 空函数
'''
def get():
    pass


def put():
    pass


def auth():
    pass


def ls():
    pass


def cd():
    pass
'''


# 2、调用函数
# 1) 语法：函数名()
# 2) 调用函数发生什么事？:
#       a. 根据函数名找到函数的内存地址
#       b. 函数的内存地址加括号可以触发函数体代码的运行
# 3) 调用函数的三种方式
# 语句
'''
def f1():
    print('from 1')

 
f1()
'''


# 表达式形式
'''
def max2(x, y):
    if x > y:
        return x
    else:
        return y


res = max(1, 2)*10
print(res)
'''


# 当作参数传给其他函数
'''
def max2(x, y):
    if x > y:
        return x
    else:
        return y


res = max2(max2(1, 2), 3)
print(res)
'''