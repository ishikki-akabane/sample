

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the homepage test!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
