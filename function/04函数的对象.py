# 函数是第一类对象，意味着函数可以当作数据去使用
import time


def foo():
    print('from foo')


# 1、可以被引用
"""
print(foo)
func = foo
print(func)
func()
"""


# 2、可以当作参数传给另外一个函数
"""
def bar(x):     # x=foo的内存地址
    print(x)
    x()


bar(foo)
"""


# 3、可以当作函数的返回值
"""
def bar():
    return foo


f = bar()
print(f is foo)
f()
"""


# 4、可以当作容器类型的元素
"""
def f1():
    print('from f1')


def f2():
    print('from f2')


vessel = [f1, f2]
print(vessel)
vessel[1]()
"""


# 练习
"""
def pay():
    print('pay function')


def withdraw():
    print('withdraw function')


def auth():
    print('auth function')


def shopping():
    print('shopping function')


def transfer():
    print('transfer function')


func_dic = {
    '1': pay,
    '2': withdraw,
    '3': auth,
    '4': shopping,
    '5': transfer
}

# print(func_dic)
# func_dic['2']()

while True:
    print('''
    0 退出
    1 支付
    2 取款
    3 认证
    4 购物
    5 转账
    ''')
    choice = input('请输入您要执行的操作：').strip()  # choice='123'
    print(choice)
    if choice == '0': break
    if choice not in func_dic:
        print('输入错误的指令，请重新输入')
        continue

    func_dic[choice]()
    time.sleep(3)
"""