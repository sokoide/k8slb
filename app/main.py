from flask import Flask, request, redirect
import os
import socket

app = Flask(__name__)


@app.route('/redirect')
def redirect_url():
    return redirect('/')


@app.route('/')
def home():
    ret = {
        "Hostname": socket.gethostname(),
    }
    headers = []
    for h in request.headers:
        headers.append(f'{h[0]}: {h[1]}')
    ret["Headers"] = headers

    envs = []
    for k, v in os.environ.items():
        envs.append(f'{k}: {v}')
    ret["Env"] = envs
    return ret


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
