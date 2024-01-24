from behave import given, when, then
from local_dev.flask_run import app


@given('I have a web client')
def step_impl(context):
    context.client = app.test_client()
    context.client.testing = True


@when('I request "{endpoint}" with parameters "a" as {a} and "b" as {b}')
def step_impl(context, endpoint, a, b):
    context.response = context.client.get(f'/{endpoint}?a={a}&b={b}')


@then('the response should be {result}')
def step_impl(context, result):
    assert context.response.status_code == 200
    assert context.response.data.decode('utf-8') == result
