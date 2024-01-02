import pytest


#@pytest.mark.skip
@pytest.mark.xfail
def test_firstcase():
    message = "Hello"
    print(message)
    assert message == "Hi","Not macthced the string"


@pytest.mark.smoke
def test_firstcase():
    print("hello world of demo1 ")


@pytest.mark.smok
def test_secondcase():
    print("good morning of demo 1")