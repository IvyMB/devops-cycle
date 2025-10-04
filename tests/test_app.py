from app.app import say_hello


def test_hello_world():
    assert say_hello() == "Hello World!"
