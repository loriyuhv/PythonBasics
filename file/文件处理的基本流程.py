# 文件处理的基本流程
"""
1、什么是文件
    文件是操作系统为应用程序或者用户提供的一个操作硬盘的虚拟单位。
2、为什么要使用文件
    应用程序中需要经常将内存的数据永久保存下来，而应用程序又无法直接操作硬件
    只能通过操作系统提供的虚拟的单位去间接地操作硬盘。
3、如何用文件

    # 会有转义字符
    # open("E:\teconology\Python\PythonBasic\file\a.txt")
    # 在字符串前加个r即可：r: rawstring 原生字符串
    # open(r"E:\teconology\Python\PythonBasic\file\a.txt", mode='r')

    # open操作做了哪些事？
    # 1、向操作系统发送打开文件的请求
    # 2、在应用程序中拿到一个返回值，该值指向操作系统打开的文件。

    f = open(r"a.txt", mode='r', encoding='utf-8')
    # f=>应用程序中的一个值=>操作系统打开的文件a.txt => 硬盘中的一块空间

    data = f.read()
    # 注意：存的时候用什么编码，取的时候用什么编码。python默认utf-8
    print(data)

    f.close()  # 向操作系统发送关闭文件的请求

    # 总结：文件处理的步骤
    # 1、打开文件
    # 2、读/写文件
    # 3、关闭文件
"""

# 上下文管理
with open(r"a.txt", mode='r', encoding='utf-8') as f:
    # 文件处理代码
    print(f.read())


