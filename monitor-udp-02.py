import socket
import struct
import time

def check_ntp_server(host, port=123):
    try:
        # 创建一个UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)

        # 构造NTP请求报文
        msg = b'\x1b' + 47 * b'\0'

        # 发送NTP请求
        sock.sendto(msg, (host, port))

        # 接收NTP响应
        try:
            data, _ = sock.recvfrom(1024)
            if data:
                print(f"Port {port} on {host} is open and responding.")
            else:
                print(f"Port {port} on {host} is open but no data received.")
        except socket.timeout:
            print(f"Port {port} on {host} might be open (no response received).")
        finally:
            sock.close()
    except Exception as e:
        print(f"Port {port} on {host} is closed or unreachable. Error: {e}")


# 示例使用
host = "ntp5.aliyun.com"
check_ntp_server(host)
