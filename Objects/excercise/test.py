class School:
    school_name = "OldBoy"

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.classes = []

    def related_class(self, class_name):
        self.classes.append(class_name)

    def print_class(self):
        print(self.name)
        for class_name in self.classes:
            print("%s\t" % class_name)


# 一：学校
# 1. 创建校区
school_obj1 = School('瑶湖校区', '南昌')
school_obj2 = School('艺超校区', '宜春')

# 2. 为学校开设班级
# 瑶湖校区
school_obj1.related_class("大数据技术与应用1班")
school_obj1.related_class("大数据技术与应用2班")
# 艺超校区
school_obj2.related_class("平面设计与应用1班")

school_obj1.print_class()
school_obj2.print_class()
# 一、定义类
"""
class Student:
    # 1. 变量的定义
    stu_school = 'OldBoy'

    # 2. 功能的定义
    def print_stu_info(self, obj):
        print("学生信息：名字：%s 年龄：%s 性别：%s" % (
            obj["stu_name"],
            obj['stu_age'],
            obj["stu_gender"],
        ))

    def set_info(self, obj, x, y, z):
        obj["stu_name"] = x
        obj["stu_age"] = y
        obj["stu_gender"] = z

    print("Hello Class!!!")
"""

# 属性访问的方法
# 1. 访问数据属性
# print(Student.stu_school)
# print(Student.__dict__['stu_school'])
# 2. 访问函数属性
# print(Student.print_stu_info)

# 2. 再调用类产生的对象

# 二、再调用类产生对象
# stu1_obj = Student()
# stu2_obj = Student()
# stu3_obj = Student()
# print(stu1_obj.__dict__)
# print(stu2_obj.__dict__)
# print(stu3_obj.__dict__)

# 为对象定义自己独有的属性
# 问题1. 代码重复
# 问题2. 属性的查找顺序

# stu1_obj.stu_name = "Jerry"
# stu1_obj.stu_age = 18
# stu1_obj.stu_gender = "male"
#
# print(stu1_obj.__dict__)
#
# stu2_obj.stu_name = "Walker"
# stu2_obj.stu_age = 20
# stu2_obj.stu_gender = "male"
#
# print(stu2_obj.__dict__)
#
# stu3_obj.stu_name = "Alan"
# stu3_obj.stu_age = 19
# stu3_obj.stu_gender = "male"
#
# print(stu3_obj.__dict__)


# 问题1. 代码重复
# 解决方案一
"""
def init(obj, x, y, z):
    obj.stu_name = x
    obj.stu_age = y
    obj.stu_gender = z


init(stu1_obj, 'Jerry', 18, 'male')
init(stu2_obj, 'Waler', 20, 'male')
init(stu3_obj, 'Alan', 30, 'female')

print(stu1_obj.__dict__)
print(stu2_obj.__dict__)
print(stu3_obj.__dict__)
"""


# 解决方案二
# class Student:
#     stu_school = "OldBoy"
#
#     # 空对象
#     def __init__(self, x, y, z):
#         self.stu_name = x
#         self.stu_age = y
#         self.stu_gender = z
#
#     def print_stu_info(self):
#         print("学生信息：名字：%s 年龄：%s 性别：%s" % (
#             self.stu_name,
#             self.stu_age,
#             self.stu_gender
#         ))
#
#     def set_info(self, x, y, z):
#         self.stu_name = x
#         self.stu_age = y
#         self.stu_gender = z


# 再调用类产生对象
# 调用类的过程又称为实例化，发生了三件事
# 1. 先产生一个空对象
# 2. python会自动调用类中的__init__方法将空对象已经调用类时括号内传入的参数一同传给__init__方法
# 3. 返回初始完的对象
# stu1_obj = Student("Jerry", 18, 'male')
# stu2_obj = Student("Walker", 20, 'male')
# stu3_obj = Student("Alan", 30, 'female')

# print(stu1_obj.__dict__)
# print(stu2_obj.__dict__)
# print(stu3_obj.__dict__)
# print(stu1_obj.stu_name)
# 类的数据属性是共享给所有对象用的，大家访问地址都一样
# print(id(Student.stu_school))
# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))

# stu1_obj.stu_school = "Apache"
# print(stu1_obj.stu_school)
# print(stu2_obj.stu_school)
# print(Student.stu_school)

# print(stu1_obj.print_stu_info())
# print(stu1_obj.set_info('Tom', 19, 'female'))
# print(stu1_obj.print_stu_info())

# print(stu1_obj.print_stu_info)
# print(stu1_obj.set_info)
#
# print(stu2_obj.print_stu_info)
# print(stu2_obj.set_info)
# Student.print_stu_info(stu1_obj)
# Student.print_stu_info(stu2_obj)
# Student.print_stu_info(stu3_obj)
# Student.print_stu_info(stu1_obj)
# Student.set_info(stu1_obj, 'Tom', 20, 'female')
# Student.print_stu_info(stu1_obj)
# print(Student.print_stu_info)
# print(stu1_obj.print_stu_info)
# print(stu2_obj.print_stu_info)
# print(stu3_obj.print_stu_info)
# stu1_obj.print_stu_info()
# stu2_obj.print_stu_info()
# stu3_obj.print_stu_info()
# stu3_obj.set_info("Daffner", 38, 'male')
# stu3_obj.print_stu_info()

a, b, c = 1, 2, 3
m = 0
if a > b:
    if a > c:
        m = a
        # print("从小到大为：%d, %d, %d" % (a, ))

    else:
        m = c
else:
    if b <= c:
        m = c
    else:
        m = b
# print("max = %f" % m)
# 1. 上面延生
# 2. 并列分支实现
# 3. 看题库，上课要提问
