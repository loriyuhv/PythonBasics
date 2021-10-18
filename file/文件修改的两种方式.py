# with open('db.txt', mode='r+t', encoding='utf-8') as f:
#     f.seek(6, 0)
#     f.write("王师维")  # 执行的是覆盖

# 文本编辑器修改文件的原理
# 1、先将文件内容全部读入内存
# 2、 在内存中修改完毕
# 3、将修改的结果覆盖写入硬盘

# 优点：在修改期间硬盘上同一时刻只有一份数据。
# 缺点：占用内存过高
# with open('db.txt', mode='rt', encoding='utf-8') as f:
#     data = f.read()
#     new_data = data.replace("你", "庆庆")
# with open('db.txt', mode='wt', encoding='utf-8') as w_f:
#     w_f.write(new_data)

# 一行一行地读，一行一行地改
# 1、以读的模式打开源文件，以写的模式打开一个临时文件，
# 2、然后for循环读取一行行内容，每读一行则修改一行，将修改的结果写入临时文件，直到把源文件都遍历完。
# 3、删除原文件，将临时文件重命名为文件名

# 优点：同一时刻在内存中只存在文件的一行内容
# 缺点：在修改期间硬盘上同一份数据会保存两份
import os

# os.rename('.db.txt.swap', 'db.txt')
with open('db.txt', mode='rt', encoding='utf-8') as src_f, \
        open('.db.txt.swap', mode='wt', encoding='utf-8') as temp_f:
    for line in src_f:
        if "你" in line:
            new_line = line.replace("你", "庆庆")
        temp_f.write(new_line)

os.remove('db.txt')
os.rename('.db.txt.swap', 'db.txt')
