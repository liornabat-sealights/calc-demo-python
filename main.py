import time
from threading import Thread
from local_dev import flask_run


def run_app_in_background():
    # Assuming flask_run.run_app() starts the Flask server
    flask_run.run_app()


import requests

# Base URL of the Flask app
base_url = 'http://127.0.0.1:8080'


def call_health():
    response = requests.get(f'{base_url}/health')
    print('/health:', response.text)


def call_base():
    response = requests.get(f'{base_url}/')
    print('/:', response.text)


def call_add(a, b):
    response = requests.get(f'{base_url}/add', params={'a': a, 'b': b})
    print('/add:', response.text)


def call_sub(a, b):
    response = requests.get(f'{base_url}/sub', params={'a': a, 'b': b})
    print('/sub:', response.text)


def call_mul(a, b):
    response = requests.get(f'{base_url}/mul', params={'a': a, 'b': b})
    print('/mul:', response.text)


def call_div(a, b):
    response = requests.get(f'{base_url}/div', params={'a': a, 'b': b})
    print('/div:', response.text)


def start():
    print("--------------Start----------------")
    flask_thread = Thread(target=run_app_in_background)
    flask_thread.daemon = True  # This ensures the thread will be killed when the main thread exits
    flask_thread.start()
    print("Waiting for 2 sec")
    time.sleep(2)
    call_health()
    print("Waiting for 2 sec")
    time.sleep(2)
    call_base()
    print("Waiting for 2 sec")
    time.sleep(2)
    call_add(1, 2)  # Example usage with a=1, b=2
    print("Waiting for 2 sec")
    time.sleep(2)
    call_sub(5, 3)  # Example usage with a=5, b=3
    print("Waiting for 2 sec")
    time.sleep(2)
    call_mul(4, 2)  # Example usage with a=4, b=2
    print("Waiting for 2 sec")
    time.sleep(2)
    call_div(8, 4)  # Example usage with a=8, b=4
    print("--------------Complete----------------")
def start_all():
    print("--------------Start----------------")
    flask_thread = Thread(target=run_app_in_background)
    flask_thread.daemon = True  # This ensures the thread will be killed when the main thread exits
    flask_thread.start()
    print("Waiting for 2 sec")
    time.sleep(2)
    call_health()
    call_base()
    call_add(1, 2)  # Example usage with a=1, b=2
    call_sub(5, 3)  # Example usage with a=5, b=3
    call_mul(4, 2)  # Example usage with a=4, b=2
    call_div(8, 4)  # Example usage with a=8, b=4
    print("--------------Complete----------------")
if __name__ == '__main__':
    start()
    start_all()
