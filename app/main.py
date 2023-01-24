from flask import Flask, request, redirect
import os
import socket
import platform
from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)


@app.route('/redirect')
def redirect_url():
    return redirect('/')

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/')
def home():
    ret = {
        "Hostname": socket.gethostname(),
        "Platform": platform.platform(),
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
    # this is not good enough to enable keep-alive
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host="0.0.0.0", port=5000, debug=True)
