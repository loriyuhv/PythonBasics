"""
1、什么是的函数的返回值
    函数的返回值是函数体代码运行的一个成果

2、什么时候用函数的返回值

3、如何用
"""

# return 值：
"""
1. 返回值没有类型限制
2. 返回值没有个数限制
    逗号分割多个值：返回一个元组
    一个值：返回一个值
    没有return：默认返回None
"""

# 没有return：默认返回None
'''
def f1():
    pass


print(f1())
'''

# return是函数结束的标志:
#   函数内可以有多个return，但只要执行一次，整个函数就立即结束，并且
#   将return后的值当作本次调用的结果返回

'''
def f1():
    print(1)
    return 'aaa'
    print(2)
    return 'bbb'
    print(3)
    return 'cccc'


print(f1())
'''





