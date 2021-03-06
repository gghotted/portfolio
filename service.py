from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('static/index.html')


@app.route('/contact', methods=['post'])
def contact():
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
