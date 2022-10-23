# 1. 什么是继承
"""
1）继承是一种创建新类的方式，在Python中，新建的类可以继承一个或多个父类，
新建的类可称为子类或派生类，父类又可称为基类或超类，子类会遗传父类的使用。
2）需要注意得是：python支持多继承
    在python中，新建的类可以继承一个或多个父类。
3）python的多继承
    优点：子类可以同时遗传多个父类的属性，最大限度地重用代码。
    缺点：
        I. 违背了人的思维习惯：继承表达的是一种什么“是”什么的关系。
        II. 代码可读性会变差
        III. 不建议使用多继承，扩展性变差
        如果真的涉及到一个子类不可避免地重用多个父类的属性，应该使用Mixins

# 基本格式
# class Parent1:
#     x = 666
#
#
# class Parent2:
#     pass
#
#
# class Sub1(Parent1):  # 单继承
#     pass
#
#
# class Sub2(Parent1, Parent2):  # 多继承
#     pass


# print(Sub1.__bases__)
# print(Sub2.__bases__)
# print(Sub1.x)

# ps：在python2中有经典类与新式类之分
# 新式类：继承了object类的子类，以及该子类的子类。。。。
# 经典类：没有继承object类的子类，以及该子类的子类。。。。
# ps2:在python3中没有继承任何类，那么会默认继承object类，所以python3中所有类都是新式类
# print(type(Sub1.__bases__))
# print(type(Sub2.__bases__))
"""

# 2. 为何要继承：用来解决类与类之间代码冗余问题，类是来解决对象之间代码冗余问题
""""""


# 3. 如何实现继承
# 示例1：类与类之间存在冗余问题
"""
class Student:
    school = "OldBoy"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def choose_course(self):
        print("%s正在选课！！！" % self.name)


class Teacher:
    school = "OldBoy"

    def __init__(self, name, age, sex, salary, level):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.level = level

    def score(self):
        print("%s正在打分！！！" % self.name)
"""


# 示例2：基于继承解决类与类之间的冗余问题
class OldboyPeople:
    school = "OldBoy"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(OldboyPeople):
    # school = "OldBoy"

    def __init__(self, name, age, sex, stu_id):
        OldboyPeople.__init__(self, name, age, sex)
        self.stu_id = stu_id
        # self.name = name
        # self.age = age
        # self.sex = sex

    def choose_course(self):
        print("%s正在选课！！！" % self.name)


class Teacher(OldboyPeople):
    # school = "OldBoy"

    def __init__(self, name, age, sex, salary, level):
        # 指名道姓地跟父类OldboyPeople去要__init__
        OldboyPeople.__init__(self, name, age, sex)
        # self.name = name
        # self.age = age
        # self.sex = sex
        self.salary = salary
        self.level = level

    def score(self):
        print("%s正在打分！！！" % self.name)


# stu_obj = Student("Jerry", 18, "male", 20197360)
# print(stu_obj.__dict__)
# print(stu_obj.school)
# stu_obj.choose_course()

tea_obj = Teacher("Tom", 26, "female", 3200, 8)
print(tea_obj.__dict__)
print(tea_obj.school)
tea_obj.score()



