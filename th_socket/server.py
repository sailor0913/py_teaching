import socket

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
print(host)

# 设置端口号
port = 12345

# 绑定端口号
s.bind((host, port))

# 设置最大连接数，超过后排队
s.listen(5)

print('服务器启动，等待客户端连接...')

while True:
    # 建立客户端连接
    c, addr = s.accept()
    print('收到来自 %s 的连接' % str(addr))

    c.send('欢迎连接'.encode('utf-8'))
    message = c.recv(1024).decode('utf-8')
    print('收到消息：', message)

    # 关闭连接
    c.close()