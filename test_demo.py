import pytest


def test_firstcase():
    print("hello world")


@pytest.mark.smoke
def test_secondcase():
    print("good morning")