import socket
import threading

def handle_client(c):
    while True:
        message = c.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            print('客户端请求断开连接。')
            c.send('连接已断开'.encode('utf-8'))
            break
        print('收到消息：', message)
        
    c.close()

# 创建 socket 对象
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
    
    client_thread = threading.Thread(target=handle_client, args=(c,))
    client_thread.start()
