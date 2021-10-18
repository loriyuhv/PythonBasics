# 将图片拷贝到D盘test
import sys
sys.argv
# src_file_path = input("源文件路径：").strip()
src_file_path = sys.argv[1]
dst_file_path = sys.argv[2]
# dst_file_path = input("目标文件路径：").strip()

with open(r'%s' %src_file_path, mode='rb') as read_f, \
        open(r"%s" %dst_file_path, mode="wb") as write_f:
    for line in read_f:
        write_f.write(line)


