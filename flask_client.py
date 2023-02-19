import requests
import time

host_ip = "127.0.0.1"
host_port = "8080"
path = "/draw"
loop = True


def main():
    # Initialize client
    URL = "".join(["http://", host_ip, ":", host_port, path])
    msg = "mov_hor"

    # Send new request(s)
    while True:
        r = requests.post(url=URL, data=msg)
        print("Flask client received:", r.text)

        if not loop:
            break

        time.sleep(1)


if __name__ == '__main__':
    main()
