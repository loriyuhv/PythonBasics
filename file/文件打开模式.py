# 文件的打开模式有三种
# r：只读模式
# w：只写模式
# a：追加模式

# 控制操作文件内容的模式有两种（不能单独使用，必须与r、w、a连用）
# t：文本模式. 默认模式. 该模式下操作文件内容的单位都是字符串. 只适用于文本文件。
    # 强调：该模式下必须指定encoding="某种字符编码"
# b：bytes二进制模式. 该模式下操作文件内容的单位都是bytes. 该模式适用于所有文件

# 1、r模式 注意：由于 默认是rt，所以一定要指定字符编码
# 文件不存在则报错
# 文件存在，并且文件指针调到文件的开头
with open('a.txt', mode='r', encoding='utf-8') as f:
    # data1 = f.read()
    # print(type(data))
    # print("第一次：", data1)
    # data2 = f.read()
    # print("第二次：", data2)
    # print(f.readable())
    # print(f.writable())
    # readline 和 readlines 的区别
    # print(f.readline(), end='') # 字符串
    # print("==>")

    # print(f.readlines())    # 列表
    pass

# 2、w模式 注意：由于 默认是wt，所以一定要指定字符编码
# 文件不存在则创建一个空文档，并且文件指针调到文件的开头
# 文件存在，会将内容清空， 并且文件指针调到文件的开头
# 强调：如果每次都是重新打开文件，那么文件内容总会清空，指针跳到开头。
# 如果在打开文件不关闭的情况下，连续的写入，本次写入会基于上一次指针所在的位置继续写
with open('b.txt', mode='wt', encoding='utf-8') as f:
    # f.write("你好啊！\n")
    # f.write("我的天！\n")
    # l = ["1111\n", "2222\n", "3333\n"]
    # f.writelines(l)
    # # 等同于：
    # for line in l:
    #     f.write(line)
    f.write("1111\n")
with open('b.txt', mode='rb') as f:
    print(f.read())

# 2、a模式: 只追加模式 注意：由于 默认是wt，所以一定要指定字符编码
# 文件不存在则创建一个空文档，并且文件指针调到文件的末尾
# 文件存在，也会将文件指针调到文件的末尾
with open('a.txt', mode='at', encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    f.write("你好！\n")
    f.writelines(["Alan\n", "Fanny\n"])