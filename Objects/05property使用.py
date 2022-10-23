# 什么是装饰器
"""
装饰器是在不修改被装饰对象源代码以及调用方式的前提下为被装饰对象添加新功能的可调用对象
print(property)
"""


# property是一个装饰器，是用来干什么？
# 是用来绑定给对象的方法伪造成一个数据属性

# 案例一
'''
"""
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）÷身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86
"""
class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.height = height
        self.weight = weight

    # 定义函数的原因1：
    # 1. 从bmi的公式上看，bmi是应该触发功能计算得到的
    # 2. bmi是随着身高、体重的变化而动态变化的，不是一个固定的值
    # 说白了，每次都是需要临时计算得到的
    # 但是bmi听起来更像是一个数据属性，而非功能
    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


person01 = People("Jerry", 59, 1.72)
print("%.2f" % person01.bmi)
'''


# 案例二
"""
class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, val):
        if type(val) is not str:
            print("不是字符型！！！")
            return
        self.__name = val

    def del_name(self):
        print("权限不够！！！")


person01 = People("Alan")
print(person01.get_name())
person01.set_name("Walker")
print(person01.get_name())
person01.del_name()
print(person01.get_name())

# 根据人的需求，你更希望是person01.name 而不是person01.get_name
# 改进一
class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, val):
        if type(val) is not str:
            print("不是字符型！！！")
            return
        self.__name = val

    def del_name(self):
        print("权限不够！！！")

    name = property(get_name, set_name, del_name)


person01 = People("Alan")
# print(person01.get_name())
print(person01.name)
# person01.set_name("Walker")
person01.name = "Walker"
# print(person01.get_name())
print(person01.name)
# person01.del_name()
del person01.name
# print(person01.get_name())
print(person01.name)
"""


# 改进二 推荐
class People:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if type(val) is not str:
            print("不是字符型！！！")
            return
        self.__name = val

    @name.deleter
    def name(self):
        print("权限不够！！！")


person01 = People("Alan")
# print(person01.get_name())
print(person01.name)
# person01.set_name("Walker")
person01.name = "Walker"
# print(person01.get_name())
print(person01.name)
# person01.del_name()
del person01.name
# print(person01.get_name())
print(person01.name)
