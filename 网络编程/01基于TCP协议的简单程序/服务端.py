import socket

# 1. 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM 流式协议 =》tcp协议 SOCK_DGRAM 数据报协议

# 2.绑定手机卡
phone.bind(('127.0.0.1', 8080))
# 端口：0-65535，1024以前的都被系统保留使用

# 3. 开机
phone.listen(5)  # 5指的是半链接池的大小
# print("服务端启动完成，监听地址为%s:%s" % ('127.0.0.1', 8080))

# 4. 等待电话连接请求：拿到电话连接conn
while True:
    conn, client_addr = phone.accept()
    # print(conn)
    print("客户端的ip和端口：", client_addr)

    # 5. 通信：收\发消息
    data = conn.recv(1024)  # 最大接收的数据量为1024Bytes，收到的是bytes类型
    print("客户端发来的消息：", data.decode("utf-8"))
    conn.send(data.upper())

    # 6. 关闭电话连接
    conn.close()

# 7. 关机（可选）
# phone.close()



