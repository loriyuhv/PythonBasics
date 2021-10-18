# 文件内指针操作 f.seek
# f.seek：单位统一就是字节
# 第一个参数：控制移动的字节数
# 第二个参数：控制移动的参照物，值可以是0、1、2
# 0：参照文件开头
# 1：参照当前位置
# 2：参照文件末尾
""""""
# 0：参照文件开头 （在b和t模式下都可用）

# with open('d.txt', mode='rt', encoding='utf-8') as f:
#     # f.seek(2)   # 单位是字节
#     print(f.read())
#     f.seek(0, 0)
#     print("第二次", f.read())

# 1：参照当前位置 （只能在b模式下用）

# 储备：read(n) t模式下
# read的n在t模式下代表的是字符个数
# read的n在b模式下代表的是字节个数
# 其余所有文件内指针的移动都是以字节为单位

# with open('d.txt', mode='rb') as f:
#     # data = f.read(3)
#     # print(data)
#     s = f.read(3)
#     print(s)
#     # print(f.tell())  # 查看当前指针位置
#     f.seek(3, 1)
#     print(f.read().decode('utf-8'))

# 注意：python里：中文：utf-8占3个字节，gbk占2个字节
# utf-8: 你好 bytes：b'\xe4\xbd\xa0\xe5\xa5\xbd'
# gbk: 你好 bytes：b'\xc4\xe3\xba\xc3'

# with open('e.txt', mode='wt', encoding='gbk') as w_f:
#     w_f.write("你好")
#
# with open('e.txt', mode='rb') as l:
#     print(l.read())

# 2：参照文件末尾（只能在b模式下用）
with open('d.txt', mode='rb') as f:
    f.seek(-5, 2)
    print(f.read())
