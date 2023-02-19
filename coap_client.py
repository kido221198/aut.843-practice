from coapthon.client.helperclient import HelperClient
import time

host = "127.0.0.1"
port = 5683
path = "draw"
loop = True


def main():
    # Initialize client
    client = HelperClient(server=(host, port))

    # Send new request(s)
    while True:
        msg = client.post(path, 'mov_ver')
        print("CoAP client received:", msg)

        if not loop:
            break

        time.sleep(1)

    # Demolish client
    client.stop()


if __name__ == '__main__':
    main()
