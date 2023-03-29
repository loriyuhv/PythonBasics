# class Student:
#     __school = "OldBoy"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name + ":" + str(self.age))
#
#
# student01 = Student("Alan", 18)
# student02 = Student("Jerry", 20)
#
# print(Student.__dict__)


class Student:
    __school = "OldBoy"

    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


student01 = Student("Alan", "male", 18)

student01.set_name("Jerry")
print(student01.get_name())





