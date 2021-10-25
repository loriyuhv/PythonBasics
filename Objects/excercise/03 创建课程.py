class School:
    school_name = "OldBoy"

    def __init__(self, nickname, addr):
        self.nickname = nickname
        self.addr = addr
        self.classes = []

    def related_class(self, class_obj):
        # self.classes.append(class_name)
        self.classes.append(class_obj)

    def print_class(self):
        print(self.nickname.center(18, "="))
        for class_name in self.classes:
            # print("     %s" % class_name)
            class_name.print_course()


# 一：学校
# 1. 创建校区
school_obj1 = School('瑶湖校区', '南昌')
school_obj2 = School("艺超校区", '宜春')
'''
# 2. 为学校开设班级
# 南昌校区开了：脱产14期，南昌校区开了脱产15期
school_obj1.related_class("脱产14期")
school_obj1.related_class("脱产15期")

# 宜春校区开了：脱产29期
school_obj2.related_class("脱产29期")

# 3. 查看每个校区开设的班级
school_obj1.print_class()
school_obj2.print_class()
'''


class Class:
    def __init__(self, name):
        self.name = name
        self.course = None

    def related_course(self, course_obj):
        self.course = course_obj

    def print_course(self):
        print(self.name)
        # print("班级名：%s 课程名：%s" % (self.name, self.course))
        print('<课程名：%s 周期：%s 价钱：%s>' % (self.course.name, self.course.period, self.course.price))


# 二：班级
# 1. 创建班级
class_obj1 = Class('脱产14期')
class_obj2 = Class('脱产15期')

# 2. 为班级关联一个课程
# class_obj1.related_course("python全栈开发")
# class_obj2.related_course("Linux运维")

# 3. 查看班级开设的课程
# class_obj1.print_course()
# class_obj2.print_course()

# 4. 为学校开设班级
# 南昌校区开了：脱产14期，南昌校区开了脱产15期
school_obj1.related_class(class_obj1)
school_obj1.related_class(class_obj1)

# print(school_obj1.classes)
# 宜春校区开了：脱产29期
school_obj2.related_class(class_obj2)

# school_obj1.print_class()
# school_obj2.print_class()


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def print_course_info(self):
        print('<课程名：%s 周期：%s 价钱：%s>' % (self.name, self.period, self.price))


# 三：课程
# 1. 创建课程
course_obj1 = Course("python全栈开发", "3months", 20000)
course_obj2 = Course("Linux运维", '1months', 18000)

# 2. 查看课程的详细信息
# course_obj1.print_course_info()
# course_obj2.print_course_info()

# 2. 为班级关联一个课程
class_obj1.related_course(course_obj1)
class_obj2.related_course(course_obj2)

# 3. 查看课程的详细信息
class_obj1.print_course()
class_obj2.print_course()
