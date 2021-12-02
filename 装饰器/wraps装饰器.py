import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print("Runtime is %s" % (stop-start))
        return res
    # wrapper.__doc__ = func.__doc__
    # wrapper.__name__ = func.__name__
    return wrapper


@timer
def index():
    """
    这是一个index函数
    :return:
    """
    print("Welcome to index page!")
    time.sleep(1)


# 访问函数注释信息
# print(help(index))
# print(index.__doc__)


# 三元表达式
# 语法：
# 条件成立时返回值 if 条件 else 条件不成立时返回值

# 例一：
x = 10
y = 8

res = x if x > y else y
# print(res)

# 列表生成式
number = []
for i in range(10):
    if i > 3:
        number.append(i)

# print(number)

# 虽然可以无限套用，但为了保证程序的可读性，最多加个if即可
number02 = [i for i in range(10) if i > 3]
# print(number02)

# 例2
names = ["jerry_sb", "tom_sb", "walker_sb"]
l = []
for name in names:
    if name.endswith('sb'):
        l.append(name.strip("_sb").title())

names02 = l
# print(names02)

names03 = [name.strip("_sb").title() for name in names if name.endswith("_sb")]
# print(names03)

# 字典生成式
info = [
    ["name", "jerry"],
    ("age", 18),
    ["sex", "male"]
]
d = {}
for item in info:
    d[item[0]] = item[1]

print(d)

student = {item[0]: item[1] for item in info}
print(student)
# 生成器表达式

i = {
    "name": "egon",
    "age": 18,
    "sex": "male"
}

i = {k.title(): v for k, v in i.items()}
print(i)

