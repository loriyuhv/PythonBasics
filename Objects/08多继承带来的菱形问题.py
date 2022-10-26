# 一、菱形问题与mro介绍
"""
class A(object):
    def test(self):
        print("from A")


class B(A):
    def test(self):
        print("from B")


class C(A):
    def test(self):
        print("from C")


class D(B, C):
    pass


obj = D()
print(D.mro())  # 类D以及该类C的对象访问属性都是参照该类的mro列表。
# obj.test()

obj_c = C()
# print(C.mro())  # 类D以及该类C的对象访问属性都是参照该类的mro列表。
# obj_c.test()
# 总结：类相关的属性查找（类名.属性，该类的对象.属性），都是参照该类的mro。

"""


# 二、非菱形多继承下的属性查找顺序，经典类和新式类属性查找顺序一样
# 都是一个分支一个分支地找下去，最后找object
"""
class E:
    def test(self):
        print('from E')


class F:
    def test(self):
        print('from F')


class B(E):
    def test(self):
        print('from B')


class C(F):
    def test(self):
        print('from C')


class D:
    def test(self):
        print('from D')


class A(B, C, D):
    # def test(self):
    #     print('from A')
    pass


obj = A()
print(A.mro())
"""


# 三、菱形多继承下的属性查找顺序，属性查找顺序不一样
# 经典类：深度优先，会在检索第一条分支的时候就直接一条道走到黑，即会检索大脑袋（共同的父类）
# 新式类：广度优先，会在检索最后一条分支的时候检索大脑袋（共同的父类）
class G:   # 在python2中，未继承object的类及其子类，都是经典类
    def test(self):
        print('from G')


class E(G):
    # def test(self):
    #     print('from E')
    pass


class F(G):
    def test(self):
        print('from F')


class B(E):
    # def test(self):
    #     print('from B')
    pass


class C(F):
    # def test(self):
    #     print('from C')
    pass


class D(G):
    # def test(self):
    #     print('from D')
    pass


class A(B, C, D):
    # def test(self):
    #     print('from A')
    pass


obj = A()
obj.test()

# 总结：
# 多继承到底要不要用？
# 要用，但要规避几点问题
# 1、继承结构尽量不要过于复杂
# 2、推荐使用mixins机制：要在多继承的背景下满足什么”是“什么的关系




