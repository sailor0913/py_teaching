import socket
import threading

def receive_messages(s):
    while True:
        try:
            print('收到回复：', s.recv(1024).decode('utf-8'))
        except ConnectionResetError:
            print("服务器断开连接")
            break

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置服务器的主机名或 IP 地址
host = '服务器的IP地址或主机名'

# 设置端口号
port = 12345

# 连接服务，指定主机和端口
s.connect((host, port))

print(s.recv(1024).decode('utf-8'))

recv_thread = threading.Thread(target=receive_messages, args=(s,))
recv_thread.start()

while True:
    message = input('请输入消息：')
    try:
        s.send(message.encode('utf-8'))
    except BrokenPipeError:
        print("无法发送消息，服务器已断开连接")
        break

# 关闭连接
s.close()
