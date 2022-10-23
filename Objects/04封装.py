# 一：封装介绍
"""
封装是面向对象三大特性最核心的一个特性
封装 <==> 整合
"""

# 二、将封装的属性进行隐藏操作
# 1. 如何隐藏：在属性名前加__前缀，就会实现一个对外隐藏属性效果
"""
# code
class Student:
    __age = 18      # _Student__age

    def __f(self):  # _Student__f
        print("Test!!!")


print(Student.__dict__)
"""

# 该隐藏需要注意的问题：
"""
1）在类外部无法直接访问双下滑线开头的属性，但知道了类名和属性名就可以拼出名字：
_类名__属性，然后就可以访问了，如Foo._Student__age，所以说这种操作并没有严格
意义上地限制外部访问，仅仅只是一种语法意义上的变形。
# code
class Student:
    __age = 18     # _Student__age

    def __f(self):  # _Student__f
        print("from test")


print(Student.__dict__)
print(Student._Student__age)

2） 这种隐藏对外不对内：在类内部是可以直接访问双下滑线开头的属性的，比如self.__f()，
因为在类定义阶段类内部双下滑线开头的属性统一发生了变形。
# code
class Student:
    __age = 18     # _Student__age

    def __f(self):  # _Student__f
        print("from test")

    def f2(self):
        print(self.__age)     # print(self._Student__age)
        print(self.__f)     # print(self._Student__f)


obj = Student()
obj.f2()
3) 这种变形操作只在检查类体语法的时候发生一次，之后定义的__开头的属性都不会变形
# code
class Student:
    __age = 1     # _Student__age

    def __f(self):  # _Student__f
        print("from test")

    def f2(self):
        print(self.__age)     # print(self._Student__x)
        print(self.__f)     # print(self._Student__f)


Student.__y = 3
print(Student.__dict__)

# 访问例子
# class Student:
#     __x = 1
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#
# obj = Student("Jerry", 18)
# print(obj.__dict__)
# print(obj.name, obj.age)
"""

# 2. 为何要隐藏？
"""
1）隐藏数据属性
# code
# 设计者：Jerry
class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        # 通过该接口就可以间接地访问到名字属性
        print(self.__name)

    def set_name(self, name_val):
        if type(name_val) is not str:
            print("错误！请输入字符串")
        else:
            self.__name = name_val


# 使用者：Tom
person01 = People("Alan")
# print(person01.name)    # 无法直接用名字属性
person01.set_name(18)
person01.get_name()

2）隐藏函数/方法属性
# code
class ATM:

    def __card(self):   # 插卡
        print('插卡')

    def __auth(self):   # 身份认证
        print('用户认证')

    def __input(self):  # 输入金额
        print('输入取款金额')

    def __print_bill(self):  # 打印小票
        print('打印账单')

    def __take_money(self):  # 取钱
        print('取款')

    def withdraw(self):  # 取款功能
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


obj = ATM()
obj.withdraw()
"""




