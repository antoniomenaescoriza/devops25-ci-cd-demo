from app import add, multiply


def test_add():
	assert add (10, 5) == 15


def test_multiply():
	assert multiply(10, 5) == 50
