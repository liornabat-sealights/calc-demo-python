from flask import Flask, request
import logging
from service import calc

app = Flask(__name__)
log = logging.getLogger(__name__)


@app.route('/health', methods=['GET'])
def health():
    print("Health check------------------------------------------")
    return "OK"


@app.route('/', methods=['GET'])
def base():
    return "OK"


@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Error: Please provide valid integer values for the 'a' and 'b' parameters."

    return calc.add(a, b)


@app.route('/sub', methods=['GET'])
def sub():
    a = request.args.get('a')
    b = request.args.get('b')

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Error: Please provide valid integer values for the 'a' and 'b' parameters."

    return calc.sub(a, b)


@app.route('/mul', methods=['GET'])
def mul():
    a = request.args.get('a')
    b = request.args.get('b')

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Error: Please provide valid integer values for the 'a' and 'b' parameters."

    return calc.mul(a, b)


@app.route('/div', methods=['GET'])
def div():
    a = request.args.get('a')
    b = request.args.get('b')

    try:
        a = int(a)
        b = int(b)
        print(a, b)
    except ValueError:
        return "Error: Please provide valid integer values for the 'a' and 'b' parameters."

    return calc.div(a, b)


def run_app():
    app.run(host='0.0.0.0', port=8080)


def get_app():
    return app
if __name__ == '__main__':
    run_app()
