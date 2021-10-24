# 一：先定义类
# 基础
"""
类是对象相似数据与功能的集合体
所以类体中最常见的是变量与函数的定义，但是类体其实是可以任意其他代码的
注意：类体代码是在类定义阶段就会立即执行，会产生类的名称空间
"""


# 定义类
"""
class Student:
    # 1. 变量的定义
    stu_school = 'OldBoy'

    # 2. 功能的定义
    def print_stu_info(obj):
        print("学生信息：名字：%s 年龄：%s 性别：%s" % (
            obj["stu_name"],
            obj['stu_age'],
            obj["stu_gender"],
        ))

    def set_info(obj, x, y, z):
        obj["stu_name"] = x
        obj["stu_age"] = y
        obj["stu_gender"] = z

    # print("Hello Class")


# print(Student.__dict__)
"""

# 属性访问的语法
"""
# 1、访问数据属性
print(Student.stu_school)   # print(Student.__dict__['stu_school'])

# 2、访问函数属性
print(Student.print_stu_info)   # print(Student.__dict__['print_stu_info'])
"""

# 二、再调用类产生对象
"""
stu1_obj = Student()
stu2_obj = Student()
stu3_obj = Student()

# print(stu1_obj.__dict__)
# print(stu2_obj.__dict__)
# print(stu3_obj.__dict__)
"""

# 为对象定制自己独有的属性
# 问题1：代码重复
# 问题2：属性的查找顺序
"""
stu1_obj.stu_name = "Jerry"     # stu1_obj.__dict__["name"] = "Jerry"
stu1_obj.stu_age = 18   # stu1_obj.__dict__["stu_age"] = 18
stu1_obj.stu_gender = "male"    # stu1_obj.__dict__["stu_gender"] = "male"

print(stu1_obj.__dict__)

stu2_obj.stu_name = "Walker"
stu2_obj.stu_age = 20
stu2_obj.stu_gender = "male"

print(stu2_obj.__dict__)

stu3_obj.stu_name = "Alan"
stu3_obj.stu_age = 19
stu3_obj.stu_gender = "male"

print(stu3_obj.__dict__)
"""


# 解决问题一：
# 解决方案一：
"""
def init(obj, x, y, z):
    obj.stu_name = x
    obj.stu_age = y
    obj.stu_gender = z


init(stu1_obj, 'Jerry', 18, 'male')
init(stu2_obj, 'Walker', 19, 'male')
init(stu3_obj, 'Alan', 20, 'male')


print(stu1_obj.__dict__)
print(stu2_obj.__dict__)
print(stu3_obj.__dict__)
"""


# 解决方案二：
# 一：定义类
class Student:
    # 1. 变量的定义
    stu_school = 'OldBoy'

    # 空对象, 'Jerry', 18, 'male'
    def __init__(obj, x, y, z):
        obj.stu_name = x    # 空对象.stu_name = 'Jerry'
        obj.stu_age = 18    # 空对象.stu_age = 18
        obj.stu_gender = 'male'     # 空对象.stu_gender = 'male'

    # 2. 功能的定义
    def print_stu_info(obj):
        print("学生信息：名字：%s 年龄：%s 性别：%s" % (
            obj["stu_name"],
            obj['stu_age'],
            obj["stu_gender"],
        ))

    def set_info(obj, x, y, z):
        obj["stu_name"] = x
        obj["stu_age"] = y
        obj["stu_gender"] = z


# 再调用类产生对象
'''
调用类的过程又称之为实例化，发生了三件事
    1. 先产生一个空对象
    2. python会自动调用类中的__init__方法将空对象已经调用类时括号内传入的参数一同传给__init__方法
    3. 返回初始完的对象
'''
stu1_obj = Student('Jerry', 18, 'male')
stu2_obj = Student('Walker', 19, 'male')
stu3_obj = Student('Alan', 20, 'male')

print(stu1_obj.__dict__)
print(stu2_obj.__dict__)
print(stu3_obj.__dict__)

# 总结__init__方法
'''
1. 会在调用类时自动触发执行，用来为对象初始化自己独有的数据
2. __init__内应该存放为对象初始化属性的功能，但是是可以存放其他代码，想要在类调用
    时就立刻执行的代码都可以放到该方法内
3. __init__方法必须返回None
'''



