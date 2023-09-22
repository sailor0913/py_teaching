import socket
import threading

def receive_messages(c):
    while True:
        try:
            message = c.recv(1024).decode('utf-8')
            if not message:
                break
            print('收到消息：', message)
        except ConnectionResetError:
            print("客户端断开连接")
            break

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

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
    
    recv_thread = threading.Thread(target=receive_messages, args=(c,))
    recv_thread.start()

    while True:
        message = input('请输入消息：')
        try:
            c.send(message.encode('utf-8'))
        except BrokenPipeError:
            print("客户端断开连接")
            break
