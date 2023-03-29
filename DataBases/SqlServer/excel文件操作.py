import xlrd2
import re
import random

filename = r'E:\z_loriyuhv\Documents\Tencent Files\2385923602\FileRecv\大学生军事技能训练(1).xlsx'
# 文件名以及路径，如果路径或者文件名有中文给前面加一个 r
data = xlrd2.open_workbook(filename)
# print(data)
# table = data.sheets()[0]
# print(table)
# names = data.sheet_names()
# print(names)
#
# name_list = [str(table.cell_value(i, 3)) for i in range(1, nrows)]

# table = data.sheets()[1]
# print(table)
# table = data.sheet_by_index(0)
# print(table)
# names = data.sheet_names()
# print(names)
# table = data.sheets()[0]
# nrows = table.nrows
# # print(nrows)
# a = table.row(1)
# # print(type(a[0]))
# b = table.row_slice(1)
# print(type(b), type(a))

table = data.sheet_by_index(0)
value = table.cell_value(1, 0)
print(value)

nrows = table.nrows

name_list = [{
    "学生姓名": str(table.cell_value(i, 0)),
    "学生学号": str(table.cell_value(i, 1)),
    "学生年龄": random.randint(18, 21),
    "学生性别": random.choices(["男", "女"], weights=[5, 1]),
    "课程名称": str(table.cell_value(i, 2)),
    "学生院系": str(table.cell_value(i, 4)),
    "学生专业": str(table.cell_value(i, 5)),
    "学生班级": str(table.cell_value(i, 6)),
    "学生成绩": str(table.cell_value(i, 7)),
}
    for i in range(nrows - 1, nrows)
    # if re.match("...", str(table.cell_value(i, 0)))
    #    and float(table.cell_value(i, 7)) > 20
    #    and str(table.cell_value(i, 4)) == '信息与人工智能学院'
    #    and str(table.cell_value(i, 6)) == '信息B2261班'
]
for i in name_list:
    print(i)
# n = 1
# for i in name_list:
#     if n % 2 and n < 20:
#         print("%s %s %s %s %s %s %s %s %s"
#               % (i["学生姓名"], i["学生学号"], i["学生年龄"], i["学生性别"], i["课程名称"],
#                  i["学生院系"], i["学生专业"], i["学生班级"], i["学生成绩"])
#               )
#     n += 1

for i in data:
    sql_insert = "insert into Student(StuNu, StuName, StuSex, StuAge, Studept) Values ('%s, %s, %s, %d, %s')"
    cur.execute(sql_insert, (i['学生学号'], i['学生姓名'], i['学生性别'], i['学生年龄'], i['学生院系']))
    con.commit()