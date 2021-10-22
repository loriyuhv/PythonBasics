"""
1. 什么是装饰器
    装饰：为被装饰的对象添加功能
    器：工具

    装饰器本身可以是任意可调用的对象
    被装饰的对象也可以是任意可调用的对象
目标：
    写一个函数用来为另一个函数添加新功能，需要遵循开放封闭原则
        开放封闭：对修改是封闭的，对扩展是开放的
        1）不修改被装饰对象的源代码
        2）不修改被装饰对象的调用方式
"""
import time

import requests


def index():
    time.sleep(3)
    print("Welcome to index page")


# 实现统计代码运行时间
"""
start = time.time()
index()
stop = time.time()
print("run time is %s" % (stop - start))
"""


# 用闭包函数实现 这样以后统计时间不用重复使用了
"""
def count_time(func):   # func => 最原始的index
    def count(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        stop = time.time()
        print("the run is %s" % (stop - start))
        return response
    return count


# index --> count
index = count_time(index)   # index = count count包着最原始的index
index()     # count()


def sum(x, y):
    return x + y


a = count_time(sum)
print(a(2, 3))  # none
"""


# 装饰器的语法糖: 在被装饰对象正上方单独一行写上@装饰器名字
"""
def runtime(func):
    def count(*args, **kwargs):
        start_time = time.time()
        response = func(*args, **kwargs)
        stop_time = time.time()
        print("the run-time is %s." % (stop_time - start_time))
        return response
    return count


@runtime    # get_data = runtime(index)
def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("OK")


@runtime    # sum = runtime(sum)
def sum(x, y):
    return x + y


get_data = runtime(get_data)
get_data("http://www.baidu.com")
"""


