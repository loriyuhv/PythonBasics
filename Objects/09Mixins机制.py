# 多继承的正确打开方式：Mixins机制
# Mixins机制核心：就是在多继承背景下尽可能地提升多继承的可读性
# ps:"让多继承满足人的思维习惯=> 什么”是“什么
# 就像常量的定义一样，PI = 3.1415926，没有改变变量的本质，但提升了命名/编写规范。

class Vehicle:
    pass


class FlyAbleMixin:
    def fly(self):
        print("I am flying!!!")


class CivilAircraft(FlyAbleMixin, Vehicle):   # 民航飞机
    pass


class Helicopter(FlyAbleMixin, Vehicle):  # 直升飞机
    pass


class Car(Vehicle):     # 汽车不会飞，但按照上述继承关系，汽车也能飞了
    pass





