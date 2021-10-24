# 面向过程和面向对象
"""
面向过程：
    核心是“过程”二字

    过程的终极奥义就是将程序流程化
    过程是“流水线”，用来分步骤解决问题的

面向对象：
    核心是“对象”二字
    对象的终极奥义就是将程序“整合”
    对象是“容器”，用来盛放数据与功能
"""
# 程序 = 数据 + 功能

# eg1: 数据和功能（普通）
"""
# 学生的数据
stu_name = "Jerry"
stu_age = 18
stu_gender = 'male'


# 学生的功能
# 打印学生信息
print("名字：%s 年龄：%s 性别：%s" % (stu_name, stu_age, stu_gender))

# 更改学生信息
stu_name = "Walker"
stu_age = 20
stu_gender = "male"

print("名字：%s 年龄：%s 性别：%s" % (stu_name, stu_age, stu_gender))
"""

# eg2：数据和功能（函数）
"""
# 学生的数据
stu_name = "Jerry"
stu_age = 18
stu_gender = 'male'


# 学生的功能
def print_info():
    print("名字：%s 年龄：%s 性别：%s" % (stu_name, stu_age, stu_gender))


def set_info(x, y, z):
    global stu_name
    global stu_age
    global stu_gender
    
    stu_name = x
    stu_age = y
    stu_gender = z

# 课程的数据
course_name = 'python'
course_period = '6months'
course_score = 10


# 课程的功能
def print_course_info():
    print("课程信息：名字：%s 周期：%s 学分：%s" % (course_name, course_period, course_score))


print_info()
set_info("Walker", 20, "male")
print_info()
print_course_info()
"""


# eg3:
"""
# 学生的功能
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


# 学生的数据
stu_obj = {
    "stu_name": "Jerry",
    "stu_age": 20,
    "stu_gender": "male",
    "print_stu_info": print_stu_info,
    "set_info": set_info
}
"""

# 学生的容器 = 学生的数据 + 学生的功能
# 课程的容器 = 课程的数据 + 课程的功能

# 化妆
# 粉扑、眼影、各种颜料 ==> 原材料 <==> 数据
# 眉笔、刷子、各种工具 ==> 小工具 <==> 功能

# python这门语言到底提供了什么语法来允许我们将数据与功能很好的整合
