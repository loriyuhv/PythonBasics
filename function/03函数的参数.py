# 1. 形参与实参
"""
1、函数的参数分为两大类：形参与实参
    形参：指的是在定义函数时，括号指定的参数,本质就是变量名
    实参：指的是在调用函数时，括号内传入的值，本质就是值

    只有在调用函数时才会在函数体内发生实参（值）与形参（变量名）的绑定关系
    该绑定关系只在调用函数时临时生效，在调用函数结束后就解除绑定


def foo(x, y):   # x=1，y=2
    print(x)
    print(y)


# a = 1
# b = 2
# foo(a, b)
foo(1, 2)
"""

# 2. 位置参数
"""
2、位置参数：
    位置形参：在定义函数时，按照从左到右的顺序依次定义的形参称之为位置形参
        注意：
            1、但凡是按照位置定义的形参，在调用函数时必须其传值，多一个不行少一个也不行

    位置实参: 在调用函数时，按照从左到右的顺序依次传入的值
        注意：
            1、在传值是按照顺序与形参一一对应


def foo(x, y, z):
    print(x, y, z)


# foo(1, 2)
# foo(1, 2, 3, 4)
# foo(1, 2, 3)
# foo(3, 2, 1)
"""

# 3. 关键字实参
"""
3、关键字实参：
    在调用函数时，按照key=value的形式定义的实参，称之为关键字实参
        注意：
            1、在传值时可以完全打乱顺序，但仍然能指定道姓地为指定的参数传值
            2、可以在调用函数时，混合使用位置实参与关键字实参
                但是位置实参必须跟在关键字实参左边
                并且不能为一个形参重复传值


def register(name, sex, age):
    print(name)
    print(sex)
    print(age)


# register('egon', 'male', 18)
# register('male', 'egon', 18)

# register('egon', 'male', 18)
# register(sex='male', name='egon', age=18)
# register('egon', age=18, sex='male')
# register(name='egon', 'male', age=18)
# register('male', name='egon', age=18)
# register('egon', age=18, sex='male')

"""

# 4. 默认参数
"""
4、默认参数：
    在定义函数时，就已经为某些参数绑定值，称之为默认参数
    注意：
        1、在定义阶段就已经有值，意味在调用阶段可以不用为其传值
        2、默认形参必须放到位置形参的后面
        3、默认形参的值只在定义阶段生效一次，在函数定义之后发生的改动无效
        4、默认形参的值通常应该是不可变类型

    默认形参vs位置形参：
        默认形参：大多数情况下值都一样
        位置形参：大多情况值都是不一样的


# eg1：
def foo(x, y, z=3):
    print(x)
    print(y)
    print(z)


foo(1, 2)
foo(1, 2, 4)


# eg2:
def register(name, age, sex='female'):
    print(name)
    print(sex)
    print(age)


# register('Jerry', 38)
# register('Tom', 48)
# register('Walker', 28)
# register('alex', 73, 'male')

# eg3:
m = 10


def foo(x, y, z=m):
    print('x:%s' % x)
    print('y:%s' % y)
    print('z:%s' % z)


m = 1111
foo(1, 2)


# eg4:
def foo(name, hobby, store=[]):
    l.append(hobby)
    print('%s 的爱好是 %s' % (name, store))


foo('egon', 'read')
foo('alex', '吹牛逼')
foo('lxx', '腰子汤')


# eg5:
def foo(name, hobby, store=None):
    if store is None:
        store = []
    store.append(hobby)
    print('%s 的爱好是 %s' % (name, store))


store1 = []
foo('egon', 'read', store1)     # store1 =['read']
foo('egon', 'music', store1)    # store1 = ['read','music']
foo('egon', ' 吟诗', store1)
foo('alex', '吹牛逼')
foo('Jerry', '腰子汤')

"""

# 5. 可变长度的参数
"""
5、可变长度的参数：
    可变长度指的是在调用函数时，函数参数的个数可以不固定

    然而实参终究是要为形参传值的，针对两种形式实参个数不固定，对应着形参也必须有两种解决方案*、**
    来分别处理溢出位置实参与溢出的关键字实参

# 1. * 会将溢出的位置实参存成元组，然后赋值给紧跟其后的变量名
# a. 形参中带*


def foo(x, y, *z):  # z=(3,4,5)
    print(x)
    print(y)
    print(z)


foo(1, 2, 3, 4, 5)


# b. 形参中带*，实参中带*, 窍门：但凡碰到实参中带*，都先将其打散成位置实参，然后考虑传值
def foo(x, y, *z):  # z=(3,4,5)
    print(x)
    print(y)
    print(z)


foo(1, 2, [3, 4, 5])    # z = ([3, 4, 5],)
foo(1, 2, *[3, 4, 5])   # foo(1, 2, 3, 4, 5) ====> z = (3,4,5)
foo(1, 2, *'hello')   # foo(1, 2, 'h', 'e', 'l', 'l', 'o') ====> z = ('h', 'e', 'l', 'l', 'o')
foo(1, *[2, 3, 4, 5])  # foo(1, 2, 3, 4, 5) ====> z = (3, 4, 5)


# c. 实参中带*, 窍门：但凡碰到实参中带*，都先将其打散成位置实参，然后考虑传值
def foo(x, y, z):
    print(x, y, z)


foo(1, 2, 3)
names = ['Egon', 'Alex', 'Jerry']
foo(*names)     # foo('Egon', 'Alex', 'Jerry')
foo(*[1, 2, 3])   # foo(1, 2, 3)


# 2. ** 会将溢出的关键字实参存成字典，然后赋值给紧跟其后的变量名


# a 形参中带**
def foo(x, y, m, n, **z):
    print(x)
    print(y)
    print(m)
    print(n)
    print(z)


foo(1, 2, n=10, m=20, a=1, b=2, c=3)    # z = {"a": 1, "b": 2, "c": 3}


# b. 形参中带**，实参中带**, 窍门：但凡碰到实参中带**，都先将其打散成关键字实参，然后考虑传值
def foo(x, y, **z):
    print(x, y, z)


foo(1, 2, **{'a': 1, 'b': 2, 'c': 2})   # foo(1, 2, c=2, a=1, b=2)
foo(1, **{'a': 1, 'b': 2, 'c': 2, 'y': 111})    # foo(1, c=2, a=1, b=2, y=111)


# c 实参中带**,
def foo(x, y, z):
    print(x, y, z)


# foo(1, **{'a': 1, 'b': 2, 'y': 111, 'z': 222})  # foo(1, b=2, a=1, y=111, z=222)
# foo(1, **{'y': 111, 'z': 222})  # foo(1, y=111, z=222)
# foo(**{'z': 1, 'y': 2, 'x': 3})     # foo(y=2, z=1, x=3)


# 如果我们的需求是
# 需要将外层的函数的参数格式原方不动地转嫁给器内部调用的函数，就需要用到下述形式
def index(name, age, sex):
    print('name:%s age:%s sex:%s' % (name, age, sex))


def wrapper(*args, **kwargs):
    # print(args, kwargs)     # args=(1, 2, 3)    kwargs={'a': 10, 'b': 20, 'c': 30}
    index(*args, **kwargs)
    # index(*(1, 2, 3),**{'a': 10, 'b': 20, 'c': 30}) # index(1, 2, 3, a=10, b=20, c=30)


wrapper(1, 2, 3, a=10, b=20, c=30)


# 我们虽然调用的是wrapper函数，但是我们遵循的其实是index函数的参数规则
def index(name, age, sex):
    print('name:%s age:%s sex:%s' % (name, age, sex))


def wrapper(*args, **kwargs):   # args=('egon',) kwargs={'sex': 'male','age': 18}
    index(*args, **kwargs)
    # index(*('egon',), **{'sex': 'male', 'age': 18})
    # index('egon', sex='male', age=18)


wrapper('egon', sex='male', age=18)


"""

# 6. 命名关键字参数
"""
命名关键字参数(了解)：但凡是在*后**之前定义的参数称之为命名关键字参数
注意点：在调用函数时，传值的形式必须是key=value


def foo(x, y, *args, m=1, n):
    print(x, y, m, n)
    print(args)


foo(1, 2, n=3, m=4)
foo(1, 2, n=3)
foo(1, 2, 3, 4, 5, n=222, m=11)

"""

# 常用形式
"""
def foo(x, y=100, *args, m, **kwargs):
    print(x, y, args, m, kwargs)


foo(1, 2, 3, 4, 5, 6, m=200, n=300, a=400)


def my_sum(*args):
    res = 0
    for item in args:
        res += item

    return res


print(my_sum(1, 2, 3, 4, 5, 6))
"""