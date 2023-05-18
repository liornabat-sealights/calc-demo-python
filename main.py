from flask import Flask, request
import logging

app = Flask(__name__)
log = logging.getLogger(__name__)


@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Error: Please provide valid integer values for the 'a' and 'b' parameters."

    return str(int(a) + int(b))


@app.route('/sub', methods=['GET'])
def sub():
    a = request.args.get('a')
    b = request.args.get('b')

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Error: Please provide valid integer values for the 'a' and 'b' parameters."

    return str(int(a) - int(b))


@app.route('/mul', methods=['GET'])
def mul():
    a = request.args.get('a')
    b = request.args.get('b')

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Error: Please provide valid integer values for the 'a' and 'b' parameters."

    return str(int(a) * int(b))


@app.route('/div', methods=['GET'])
def div():
    a = request.args.get('a')
    b = request.args.get('b')

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Error: Please provide valid integer values for the 'a' and 'b' parameters."

    return str(int(a) / int(b))


if __name__ == '__main__':
    app.run()
