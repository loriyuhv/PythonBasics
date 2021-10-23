# 函数的嵌套调用：在调用一个函数的时，其内部的代码又调用其他的函数
"""
# eg1:
def bar():
    print('from bar')


def foo():
    print('from foo')
    bar()


foo()


# eg2:
def max2(x, y):
    if x > y:
        return x
    else:
        return y


def max4(a, b, c, d):
    res1 = max2(a, b)
    res2 = max2(res1, c)
    res3 = max2(res2, d)
    return res3


print(max4(1, 2, 3, 4))
"""


# 函数的嵌套定义：在一个函数的内部又定义了另外一个函数
"""
def f1():
    x = 1

    def f2():
        print('from f2')
    print(x)
    print(f2)
    f2()


# f1 = 10
# print(f1)

# f1()
# f2()

# print(x)
"""



