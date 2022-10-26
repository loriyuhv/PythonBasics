# 在子类派生的新方法中如何重用父类的功能
# 方式一：指名道姓调用某一个类下的函数 => 不依赖于继承关系
"""
class OldboyPeople:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print("%s say hello" % self.name)


class Teacher(OldboyPeople):
    def __init__(self, name, age, sex, level, salary):
        OldboyPeople.__init__(self, name, age, sex)
        self.level = level
        self.salary = salary


tea_obj = Teacher("Jerry", 18, "male", 10, 2300)
print(tea_obj.__dict__)
"""


# 方式二：super() 调用父类提供给自己的方法 => 严格依赖继承关系
"""
# 调用super()会得到一个特殊的对象，该对象会参照发起属性查找类的mro，去
# 当前的父类中找属性
class OldboyPeople:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print("%s say hello" % self.name)


class Teacher(OldboyPeople):
    def __init__(self, name, age, sex, level, salary):
        # super(Teacher, self).__init__(name, age, sex)    # python2
        super().__init__(name, age, sex)  # python3 调用的是方法，自动传入对象
        self.level = level
        self.salary = salary


tea_obj = Teacher("Jerry", 18, "male", 10, 2300)
print(tea_obj.__dict__)
"""


# super() 案例一
"""
class A:
    print("from A")

    def test(self):
        super().test()


class B:
    def test(self):
        print("from B")


class C(A, B):
    pass


# print(A.mro())
obj = C()
print(C.mro())
obj.test()
"""


# 案例二 报错
"""
class A:
    def test(self):
        super().test1()


class B:
    def test(self):
        print("from B")


class C(A, B):
    def test1(self):
        print("from C")


# print(A.mro())
obj = C()
print(C.mro())
obj.test()
"""

