# sample flask app
# developer: iShikki-Akabane
# GitHub.com/StackHost

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the homepage test!"


if __name__ == '__main__':
    # running on 0.0.0.0 is must important
    app.run(host='0.0.0.0', port=5000)
