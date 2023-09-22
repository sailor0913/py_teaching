import socket

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = '主机用户名或者ip'

# 设置端口号
port = 12345

# 连接服务，指定主机和端口
s.connect((host, port))

print(s.recv(1024).decode('utf-8'))

# 发送消息
s.send('你好，服务器！'.encode('utf-8'))

# 关闭连接
s.close()