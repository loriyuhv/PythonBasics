import socket

# 1. 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM 流式协议 =》tcp协议 SOCK_DGRAM 数据报协议

# 2. 拨通服务端电话
phone.connect(('127.0.0.1', 8080))

# 3. 通信
phone.send("hello world!!!".encode('utf-8'))

# 4. 关闭连接(必选的回收资源的操作)
phone.close()
