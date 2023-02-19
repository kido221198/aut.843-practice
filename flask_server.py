from flask import Flask, url_for, request
from irc5_client import tcp_client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FAST-Lab'

print('Initializing TCP Client')
tcp = tcp_client()


@app.route('/draw', methods=["POST"])
def transfer():
    msg = request.data
    print("Flask server received:", msg)
    res = tcp.talker(msg)
    return res


if __name__ == '__main__':
    print('Initializing Flask server')
    app.run(host="127.0.0.1", port='8080')
