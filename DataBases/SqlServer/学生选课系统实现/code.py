import pymssql
import xlrd2
import re
import random


# 连接数据库
def conn():
    con = pymssql.connect(
        host='localhost',
        port='1433',
        database='Test01',
        charset='utf8'
    )
    if con:
        print("连接成功！！！")
    else:
        print("连接失败！！！")
    return con


# 获取数据
def get_data():
    # 获取data01的数据
    filename = r'..\data\data01.xlsx'
    data = xlrd2.open_workbook(filename)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    data = [{
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
        for i in range(2, nrows)
        if re.match("...", str(table.cell_value(i, 0)))
    ]
    # 获取大学生军事技能训练里的数据
    """
    filename = r'E:\z_loriyuhv\Documents\Tencent Files\2385923602\FileRecv\大学生军事技能训练(1).xlsx'
    # 文件名以及路径，如果路径或者文件名有中文给前面加一个 r
    data = xlrd2.open_workbook(filename)
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
        for i in range(1, nrows)
        if re.match("...", str(table.cell_value(i, 0)))
           and float(table.cell_value(i, 7)) > 20
           # and str(table.cell_value(i, 4)) == '信息与人工智能学院'
           # and str(table.cell_value(i, 6)) == '信息B2261班'
    ]
    data = name_list
    # n = 1
    # data = list()
    # for i in name_list:
    #     if n % 2 and n < 20:
    #         data.append(i)
    #         # print("%s %s %s %s %s %s %s %s %s"
    #         #       % (i["学生姓名"], i["学生学号"], i["学生年龄"], i["学生性别"], i["课程名称"],
    #         #          i["学生院系"], i["学生专业"], i["学生班级"], i["学生成绩"])
    #         #       )
    #     n += 1
    """
    return data


# 处理课程
def dw_course():
    data = get_data()
    course = []
    for i in data:
        course.append(i['课程名称'])
        course = list(set(course))
    # print(course)

    a = 1
    c = {}
    for i in course:
        if a < 10:
            d = {i: "00" + str(a)}
            c.update(d)
        elif a < 100:
            d = {i: "0" + str(a)}
            c.update(d)
        else:
            d = {i: "" + str(a)}
            c.update(d)
        a += 1
    # print(c)
    return c


# 操作
def cursor_():
    cou_nu = dw_course()
    '''
    con = conn()
    cursor = con.cursor()
    # sql = "select * from Student"
    sql_drop = "drop table Student"
    sql_create = """Create table Student (
    StuNu nchar(10) primary key not null,
    StuName nchar(10) not null,
    StuSex nchar(2) not null,
    StuAge smallint not null,
    Studept nchar(10) not null
    )"""
    cursor.execute(sql_drop)
    cursor.execute(sql_create)
    # sql_insert = "insert into Student Values ('22304', '刘宝强', '男', 18, '数学教育')"
    # cursor.execute(sql_insert)

    con.commit()
    con.close()

    #     print("成功！！！")
    # else:
    #     print("失败！！！")
    '''
    con = conn()
    cur = con.cursor()
    # 插入数据
    data = get_data()

    sql_insert_student = """insert into 
    Student(StuNu, StuName, StuSex, StuAge, Studept) 
    Values(%s, %s, %s, %s, %s)"""
    sql_insert_course = """insert into 
    Course(CouNu, CouName) 
    Values(%s, %s)"""
    sql_insert_score = """insert into 
    Score(StuNu, CouNu, grade) 
    Values(%s, %s, %s)"""
    for i in data:
        # 插入学生表
        sql_select_stu = "select StuNu from Student where StuNu='" + i['学生学号'] + "'"
        cur.execute(sql_select_stu)
        stu_nu_result = cur.fetchall()
        if not stu_nu_result:
            cur.execute(sql_insert_student,
                        (i['学生学号'], i['学生姓名'],
                         i['学生性别'], i['学生年龄'], i['学生院系']))
            con.commit()
        # 插入课程表
        sql_select_cou = "select CouNU from Course where CouNu='" + cou_nu[i['课程名称']] + "'"
        cur.execute(sql_select_cou)
        cou_nu_result = cur.fetchall()
        if not cou_nu_result:
            cur.execute(sql_insert_course,
                        (cou_nu[i['课程名称']], i['课程名称']))
            con.commit()
        # 插入成绩表
        cur.execute(sql_insert_score,
                    (i['学生学号'], cou_nu[i['课程名称']], i['学生成绩']))
        con.commit()
    con.close()
    print("插入完成")


if __name__ == "__main__":
    cursor_()

