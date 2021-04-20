from flask import Flask

app = Flask('__main__')


@app.route('/', methods=['GET'])
def home():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)