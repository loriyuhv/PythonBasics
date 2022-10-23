# def foo():  # foo = 函数的内存地址
#     print('first')
#     print('second')
#     print('hello')
#     print('third')
#
#
# # 调用阶段
# foo()
# print(foo)
# foo = 10
# foo()   # 出错

# def bar():
#     print("from bar")
#
#
# def foo():
#     print('from foo')
#     bar()
#
#
# foo()

# # 定义阶段
# def foo():
#     print('from foo')
#     bar()
#
#
# def bar():
#     print("from bar")
#
#
# # 调用阶段
# foo()

# # 定义阶段
# def foo():
#     print('from foo')
#     bar()
#
#
# # 调用阶段
# foo()
#
#
# def bar():
#     print('from bar')
# def func1():
#     print('hello1')
#     print('hello2')
#     print('hello3')
#
#
# func1()

# def func2(x, y):
#     # x = 1
#     # y = 3
#     if x > y:
#         print(x)
#     else:
#         print(y)
#
#
# func2(1, 2)
# func2(2, 3)
# func2(3, 4)

# def max2(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#     pass
#
#
# res = max(1, 2) * 10
# print(res)

# def max2(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#     pass
#
#
# res = max2(max2(1, 2), 3)
# print(res)

# # 逗号分隔多个值：返回一个元组
# def foo():
#     x = 10
#     y = 5
#     return x, y
#
#
# a = foo()
# print(type(a), a)

# def foo():
#     x = 10
#     return x
#
#
# a = foo()
# print(type(a), a)
# def foo():
#     return
#
#
# a = foo()
# print(type(a), a)
# def f1():
#     print(1)
#     return 'aaa'
# 	print(2)
#     return 'bbb'
#
#
# print(f1())

# def foo(x, y):   # x和y是实参
#     print(x)
#     print(y)
#
#
# a = 1
# b = 2
# foo(a, b)   # a和b是实参
# # foo(1, 2)

# def foo(x, y, z):
#     print(x, y, z)
#
#
# # foo(1, 2)
# # foo(1, 2, 3, 4)
# foo(1, 2, 3)
# foo(3, 2, 1)

# def register(name, sex, age):
#     print(name)
#     print(sex)
#     print(age)
#
#
# # 位置形参
# # register('Walker', 'male', 18)
# # register('male', 'Walker', 18)
#
# # 关键字参数
# # register('Walker', 'male', 18)
# # register(name='Walker', sex='male', age=18)
#
# # positional argument follows keyword argument
# # register('Walker', 'male', 18)
# # register(name='Walker', 'male', age=18)   # error
# # 不能为一个形参重复传值
# # register('male', name='Walker', age=18) # error
# # register('Walker', age=18, sex='male')

# def foo(x, y, z=3):
#     print(x, y, z)
#
#
# foo(1, 2)
# foo(1, 2, 4)


# def register(name, age, sex='female'):
#     print("name：%s, age：%d, sex：%s" % (name, age, sex))
#
#
# register("Jerry", 38)
# register("Tom", 48)
# register("Alex", 18, 'male')

# m = 10
#
#
# def foo(x, y, z=m):
#     print('x: %s' % x)
#     print('y: %s' % y)
#     print('z: %s' % z)
#
#
# m = 1111
# foo(1, 2)
# def foo(name, hobby, store=[]):
#     store.append(hobby)
#     print("%s 的爱好是 %s" % (name, store))
#
#
# foo('Jerry', 'reading')
# foo('Tom', 'running')

"""2022/9/23"""
# def count(a, b):
#     return a + b
#
#
# print(count(1, 2))
# def foo():  # foo=函数的内存地址
#     print('first')
#     print('second')
#     print("hello")
#     print('third')
#
#
# foo()
# print(foo)
# foo = 10
# foo()
# 定义阶段
# def foo():
#     print('from foo')
#     bar()
#
#
# def bar():
#     print('from bar')
#
#
# # 调用阶段
# foo()
# def foo():
#     print('from foo')
#     bar()
#
#
# # 调用阶段
# foo()
#
#
# def bar():
#     print('from bar')


# def fun01():
#     print("fun01")
#     fun02()
#
# fun01()
#
# def fun02():
#     print("fun02")
#
#
# fun01()

# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# print(max(max(1, 2), 3))

# def fun(a, b):
#     return a, b
#
#
# print(type(fun(1, 2)))
# print(fun(1, 2))
# for i in fun(1, 2):
#     print("%d\t" % i)
# def fun():
#     print("fun01\n")
#     return
# print("fun02")
# fun()

# def foo(a, b):
#     print("%d\t" % a, b)
#
#
# foo(1, 2)
# foo(1, 2, 3)

# def register(name, sex, age):
#     print("My name is " + name + ", my age is " + str(age) + "\n")
#
#
# register(sex="Walker", name="Male", age=18)

# def foo(a=1, b=2, c=3):
#     print(a, b, c)
#
# foo()
# foo(2, 4, 6)

# def foo(x, y, z):
#     print(x, y, z)


# foo(1, 2, [3, 4, 5], 2)
# foo(1, 2, *["Jerry", "Jack"])
# foo(1, 2, *"Jerry")
# foo(1, 2, 3)
# names = ['Egon', 'Alex', 'Jerry']
# foo(*names)


# def foo(x, y, m, n, **z):
#     print(x, y, m, n)
#     print(z)


# foo(1, 2, n=10, m=20, a=1, b=2, c=3)
# foo(1, 2, 3, 4, z=5)
# foo(4, 5, **{'a': 1, "b": 2, "c": 3})
# foo(**{"a": 1, "c": 2, "b": 3}, m=4, n=5, x=6, y=7)

# def foo(x, y, z, **a):
#     print(x, y, z)
#     print(a)
#
#
# # foo(1, **{'a': 1, 'b': 2, 'y': 111, 'z': 222})
# # foo(1, **{"y": 111, "z": 222})
# # foo(**{"z": 1, "y": 2, "x": 3})


# def index(name, age, sex):
#     print("name: %s, age: %s, sex:%s" % (name, age, sex))
#
#
# def wrapper(*args, **kwargs):
#     print(args, kwargs)
#     index(*args, **kwargs)
#
#
# wrapper(1, 2, 3, a=10, b=20, c=30)
#
# def index(name, age, sex):
#     print("name: %s, age: %s, sex:%s" % (name, age, sex))
#
#
# def wrapper(*args, **kwargs):
#     # print(args, kwargs)
#     index(*args, **kwargs)
#     # index(*('Egon',), **{"sex": 'male', "age": 18})
#     # index('Egon', sex='male', age=18)
#
#
# wrapper('Egon', sex='male', age=18)
#
# def foo(x, y, *args, m=1, n):
#     print(x, y, m, n)
#     print(args)


# foo(1, 2, n=3, m=4)
# foo(1, 2, n=3)
# foo(1, 2, 3, 4, 5, n=222, m=11)
# 1, 2, (3, 4, 5), 11, 222
# foo(1, 2, 3, 4)

# def foo(x, y=100, *args, m, **kwargs):
#     print(x, y, args, m, kwargs)
#
#
# foo(1, 2, 3, 4, 5, 6, m=200, n=300, a=400)
# 1, 2, (3, 4, 5, 6), 200, {"n": 300, "a": 400}

#
# def foo():
#     print("foo01")
#
#
# func = foo
# func()

# def foo(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# def bar(x):
#     print(x)
#     # print(x(2, 4))
#     print("%d" % x(2, 4))
#
#
# bar(foo)
#
# def bar():
#     return foo

# import math
# a = int(input("请输入三角形的第一条边："))
# b = int(input("请输入三角形的第二条边："))
# c = int(input("请输入三角形的第三条边："))
# s = 1/2*(a+b+c)
# area = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("此三角形的面积为:", area)

# import pymssql
# conn = pymssql.connect(host='localhost', server='LAPTOP-5GSM1609', port='61647', user='loriyuhv', password='@wsw0420', database='Student')
# if conn:
#     print("连接成功!")
# conn.close()

# import pymssql
#
# # 连接数据库
# sql = pymssql.connect(host='localhost',
#                       server='LAPTOP-5GSM1609',
#                       port='61647',
#                       user='loriyuhv',
#                       password='@wsw0420',
#                       database='Student')
# cur = sql.cursor()
#
# # 查询student表
# cur.execute("Select * from Student")
# # cur.execute("Insert Into Student(SName, Phone, Address) Values('帅庆庆','180794239866','宜春')")
# # cur.execute("Create Database Book")
#
#
# # 提交事务
# sql.commit()
#
# # 关闭数据库
# sql.close()
#
# # // 向 student 表中插入
# # cur.execute("insert into student VALUES ('小李', '男', '三年级')")

# a = 3
# b = -5
# c = 8
# a = b
# b = c
# print(a, b, c)


# print("-" * 40)
# print("姓名：王师维")
# print("职业：学生")
# print("住址：江西省南昌市红谷滩新区阁皂山大道998号。")
# print("-" * 40)




# a = 3
# b = -5
# c = 8
# a = b
# b = c
# c = a
# print(a, b, c)

# a = 1
# b = 3
# a = a+b
# b = a-b
# print(a, b)
# a = 10
# b = 4
# c = a+b
# a = b+c
# b = a+c
# c = a+b+c
# print(a, b, c)
"""
a = 12
b = 45
c = b % 10*1000 + a//10*100 + b//10*10 + a % 10
print(c)
"""
# name = str(input("请输入学生姓名："))
# number = str(input("请输入学生学号："))
# sex = str(input("请输入学生性别："))
# age = int(input("请输入学生年龄："))
# high = float(input("请输入学生身高："))
# weight = float(input("请输入学生体重："))
# print("-"*40)
# print("姓名：%s\n学号：%s\n性别：%s\n年龄：%d\n身高：%.2f\n体重：%.2f"
#       % (name, number, sex, age, high, weight))
# print("-"*40)

# name = str(input("请输入用户姓名："))
# age = int(input("请输入用户年龄："))
# address = str(input("请输入用户地址："))
# print("姓名：%s\n"
#       "年龄：%d\n"
#       "地址：%s\n"
#       % (name, age, address))

# price = float(input("请输入商品的单价："))
# number = int(input("请输入商品的数量："))
# print("商品的总价是%.2f元。" % (price * number))

# i = 10
# j = 4
# if i > j:
#     pass
# print("成立")
# a, b, c = 1, 2, 3
# if a > b:
#     if a > c:
#         b = a
#     else:
#         b = c
# elif b < c:
#     b = c
# print(b)

# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# if a > b:
#     print("两个数中最小的数是：%d" % b)
# else:
#     print("两个数中最小的数是：%d" % a)


# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# c = int(input("请输入第三个数："))
#
# if a > b:
#     if a > c:
#         print("三个数中最大的数是：%d" % a)
#     else:
#         print("三个数中最大的数是：%d" % c)
# elif b > c:
#     print("三个数中最大的数是：%d" % b)
# else:
#     print("三个数中最大的数是：%d" % c)


# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# c = int(input("请输入第三个数："))
#
# if a < b:
#     a, b = b, a
# if a < c:
#     a, c = c, a
# if b < c:
#     b, c = c, b
#
# print("三个数从小到大排序：%d %d %d" % (c, b, a))

# a = float(input("请输入第一个数："))
# b = float(input("请输入第二个数："))
# c = float(input("请输入第三个数："))
# if a < b < c:
#     print(a, b, c)
# elif a < c < b:
#     print(a, c, b)
# elif b < a < c:
#     print(b, a, c)
# elif b < c < a:
#     print(b, c, a)
# elif c < a < b:
#     print(c, a, b)
# else:
#     print(c, b, a)


