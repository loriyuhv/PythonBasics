import pymssql


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


con = conn()
cursor = con.cursor()
sql = "select StuNu from Student where StuNu = '1803030499'"

cursor.execute(sql)
result = cursor.fetchall()
if result:
    print("成功！！！")


# print(results)
# sql_insert = "insert into Student Values ('22303', '王宝强', '女', 20, '数学教育')"
# cursor.execute(sql_insert)
# con.commit()
con.close()
