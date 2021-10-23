"""
大前提：函数的作用域关系是在函数定义阶段就已经固定死的，与调用位置无关

闭包函数：
1、闭 ==>定义在函数的内部的函数
2、包 ==>该内部函数包含对其外层函数作用域名字的引用

闭包函数通常需要结合函数对象的概念，将闭包函数返回到外部使用
"""


# 函数的作用域关系在函数定义阶段就已经固定死了，与调用位置无关
"""
def outer():
    x = 100

    def inner():
        print(x)
    return inner


# 调用位置一
x = 200
f = outer()    # outer() <==> inner
f()


# 调用位置二
def foo():
    x = 300

    def bar():
        f()
    bar()


foo()
"""

# 闭包函数的基本形式

# 基本形式
'''
def outer(x):
    def inner():
        print(x)
    return inner
'''

# 通过参数给函数传值
'''
def sum(x, y):
    res = x + y
    return res


sum(1, 2)
'''


# 通过包传值
'''
def outer(x, y):
    # x = 1
    # y = 2

    def sum():
        res = x + y
        return res
    return sum


f = outer(1, 2)
print(f())
'''

# 案例
'''
import requests


def outer(url):
    def get():
        response = requests.get(url)
        if response.status_code == 200:
            print("Ok")
    return get


jd = outer('http://www.baidu.com')
jd()
jd()


# 这种方式不合适，因为占用了全局变量
x = "http://www.baidu.com"
get(x)
get(x)

y = 'https://www.jd.com'
get(y)
get(y)

# 什么情况下调用全局变量
答：多个函数调用
案例：
x = 100
def f1():
    print(x)
def f2():
    print(x)
def f3():
    print(x)
'''


