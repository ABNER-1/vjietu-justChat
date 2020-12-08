import flask

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')


# url_for('static', filename='index.html')


@app.route('/<path>')
def hello_world(path):
    print(path)
    return send_from_directory('static', path)


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
