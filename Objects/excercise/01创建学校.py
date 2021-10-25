class School:
    school_name = "OldBoy"

    def __init__(self, nickname, addr):
        self.nickname = nickname
        self.addr = addr
        self.classes = []

    def related_class(self, class_name):
        self.classes.append(class_name)

    def print_class(self):
        print(self.nickname)
        for class_name in self.classes:
            print("     %s" % class_name)


# 一：学校
# 1. 创建校区
school_obj1 = School('瑶湖校区', '南昌')
school_obj2 = School("艺超校区", '宜春')

# 2. 为学校开设班级
# 南昌校区开了：脱产14期，南昌校区开了脱产15期
school_obj1.related_class("脱产14期")
school_obj1.related_class("脱产15期")

# 宜春校区开了：脱产29期
school_obj2.related_class("脱产29期")

# 3. 查看每个校区开设的班级
school_obj1.print_class()
school_obj2.print_class()
