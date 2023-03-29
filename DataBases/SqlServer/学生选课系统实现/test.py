# Java引用类型 值传递规则同样适用于python。
"""
a = list()
for i in range(1, 5):
    a.append(i + 1)
print(a)
b = a
b[2] = 88
print(a)
"""
# test
"""
def fun():
    print("Hello world")

    def a():
        print("Hello a")
    print("Hello w")
    a()


fun()
"""
# test1
"""
s1 = {1, 2, 3, 4}
s2 = {5, 6, 7}
# s3 = s1 + s2
s1.update(s2)
s3 = s1
print(len(s1))
"""
#
"""
a = {"语文": "001", "数学": "002"}
b = "语文"
if b in a:
    print("哈啊哈")
"""
# 随机数
"""
import random

for i in range(0, 10):
    print(random.randint(18, 21))
"""
# 正则
"""
import re
# 测试正则
name = "王维"

if re.match("...", name):
    print("成功")
"""

# 1~100中偶数的和
# while
"""
i = 1
odd_sum = 0
even_sum = 0
while i < 100:
    odd_sum += i
    even_sum += i + 1
    i += 2

print("1~100中偶数的和%d" % even_sum)
print("1~100中奇数的和%d" % odd_sum)
"""
# for
"""
odd_sum = 0
even_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("1~100中偶数的和%d" % even_sum)
print("1~100中奇数的和%d" % odd_sum)
"""

