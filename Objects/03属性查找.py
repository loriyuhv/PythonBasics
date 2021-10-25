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
            obj.__dict__["stu_name"],
            obj.__dict__['stu_age'],
            obj.__dict__["stu_gender"],
        ))

    def set_info(obj, x, y, z):
        obj.__dict__["stu_name"] = x
        obj.__dict__["stu_age"] = y
        obj.__dict__["stu_gender"] = z


stu1_obj = Student('Jerry', 18, 'male')
stu2_obj = Student('Walker', 19, 'male')
stu3_obj = Student('Alan', 20, 'male')

# 类中存放的是对象共有的数据与功能
# 一：类可以访问
"""
# 1. 类的数据属性
print(Student.stu_school)
# 2. 类的函数属性
print(Student.print_stu_info)
print(Student.set_info)

print(stu1_obj.stu_name)
print(stu1_obj.stu_age)
print(stu1_obj.stu_gender)
"""

# 二：但其实类中的东西全是给对象用的

# 1. 类的数据属性是共享给所有对象用的，大家访问地址都一样
# print(id(Student.stu_school))

# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))
# print(id(stu3_obj.stu_school))

# stu1_obj.stu_school = "Apache"
# print(stu1_obj.stu_school)
#
# print(Student.stu_school)
# print(stu2_obj.stu_school)
# print(stu3_obj.stu_school)
# 为什么？就像函数一样，因为作用域
'''
# eg1：
name = "OldBoy"


def foo():
    print(name)


foo()   # 打印globals name：OldBoy


# eg2:
def foo():
    name = "Apache"
    print(name)


foo()   # 打印locals name：Apache
'''

# 2. 类中定义的函数主要是给对象用的，而且是绑定给对象的，虽然所有对象指向的都是相同的功能
#   但是绑定到不同的对象就是不同的绑定方法，内存地址各不相同。
# 类调用自己的函数属性必须严格按照函数的用法来
# print(Student.print_stu_info)
# print(Student.set_info)
#
# Student.print_stu_info(stu1_obj)
# Student.print_stu_info(stu2_obj)
# Student.print_stu_info(stu3_obj)
#
# Student.set_info(stu1_obj, 'Jerry', 28, 'Female')
# Student.print_stu_info(stu1_obj)

# 绑定方法特殊之处在于：谁来调用绑定方法就会将谁当做第一个参数自动传入
# print(Student.print_stu_info)
# print(stu1_obj.print_stu_info)
# print(stu2_obj.print_stu_info)
# print(stu3_obj.print_stu_info)

stu1_obj.print_stu_info()   # print_stu_info(stu1_obj)
stu2_obj.print_stu_info()   # print_stu_info(stu2_obj)
stu3_obj.print_stu_info()   # print_stu_info(stu3_obj)

# 列表案例
'''
names = ["Jerry", "Walker", "Alan"]     # names = list(["Jerry", "Walker", "Alan"])
scores = [99, 95, 80]   # scores = list([99, 95, 80])
# print(names.append)
# print(list.append)

# names.append("Alex")
# print(names)
# print(scores)

list.append(names, "Alex")
list.append(scores, 99)
print(names)
print(scores)
'''


