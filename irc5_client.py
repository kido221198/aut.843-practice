import socket
import time


HOST = "192.168.125.1"  # The server's hostname or IP address
PORT = 5000  # The port used by the server
ACTIONS = {"S": "01", "E": "03", "R": "02", "D": "04"}


class tcp_client(object):
    def __init__(self, host=HOST, port=PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.socket.connect((host, port))
        print('TCP client initialized!')

    def talker(self, msg):
        print("TCP client received:", msg)
        return "Success!"

        # self.socket.sendall(bytes(msg, 'UTF-8'))
        # data = self.socket.recv(1024)
        # time.sleep(1)
        # print(f"TCP received {data!r}")
        # if data == "02":
        #     print("Error: The Robot is busy with drawing")
        #     return "Failed!"
        # elif data == "00":
        #     print("Success!")
        #     return "Success!"



