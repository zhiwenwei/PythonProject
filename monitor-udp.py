import socket

def check_udp_port(host, port):
    try:
        # 创建一个UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)
        # 发送一个空的消息
        sock.sendto(b'', (host, port))
        # 接收响应
        try:
            data, _ = sock.recvfrom(1024)
            print(f"Port {port} on {host} is open. Received data: {data}")
        except socket.timeout:
            print(f"Port {port} on {host} might be open (no response received).")
        finally:
            sock.close()
    except Exception as e:
        print(f"Port {port} on {host} is closed or unreachable. Error: {e}")

# 示例使用
host = "192.168.1.145"
port = 54
check_udp_port(host, port)
