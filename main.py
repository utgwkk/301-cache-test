from flask import Flask, Response
app = Flask(__name__)


@app.route('/public')
def cache_control_public():
    resp = Response()
    resp.headers['Location'] = 'https://www.google.co.jp/'
    resp.headers['Cache-Control'] = 'public'
    resp.status_code = 301
    return resp


@app.route('/private')
def cache_control_private():
    resp = Response()
    resp.headers['Location'] = 'https://www.google.co.jp/'
    resp.headers['Cache-Control'] = 'private'
    resp.status_code = 301
    return resp


@app.route('/no-cache')
def cache_control_no_cache():
    resp = Response()
    resp.headers['Location'] = 'https://www.google.co.jp/'
    resp.headers['Cache-Control'] = 'no-cache'
    resp.status_code = 301
    return resp


@app.route('/no-store')
def cache_control_no_cache():
    resp = Response()
    resp.headers['Location'] = 'https://www.google.co.jp/'
    resp.headers['Cache-Control'] = 'no-store'
    resp.status_code = 301
    return resp
