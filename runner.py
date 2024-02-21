#
# import requests
#
# # Base URL of the Flask app
# base_url = 'http://127.0.0.1:8080'
#
# def call_health():
#     response = requests.get(f'{base_url}/health')
#     print('/health:', response.text)
#
# def call_base():
#     response = requests.get(f'{base_url}/')
#     print('/:', response.text)
#
# def call_add(a, b):
#     response = requests.get(f'{base_url}/add', params={'a': a, 'b': b})
#     print('/add:', response.text)
#
# def call_sub(a, b):
#     response = requests.get(f'{base_url}/sub', params={'a': a, 'b': b})
#     print('/sub:', response.text)
#
# def call_mul(a, b):
#     response = requests.get(f'{base_url}/mul', params={'a': a, 'b': b})
#     print('/mul:', response.text)
#
# def call_div(a, b):
#     response = requests.get(f'{base_url}/div', params={'a': a, 'b': b})
#     print('/div:', response.text)
#
#
#
# def start():
#     flask_run.run_app()
#
#
#
# if __name__ == '__main__':
#     call_health()
#     call_base()
#     call_add(1, 2)  # Example usage with a=1, b=2
#     call_sub(5, 3)  # Example usage with a=5, b=3
#     call_mul(4, 2)  # Example usage with a=4, b=2
#     call_div(8, 4)  # Example usage with a=8, b=4