import pytest


@pytest.mark.parametrize('i', ['P', 'y', 't', 'h', 'o', 'n'])
def test_is_str(i):
    """
    :param i: list of string
    """
    assert isinstance(i, str)


class TestEqual:
    def test_equal_add(self):
        s = 'Hello, world!'
        assert 'Hello, ' + 'world!' == s

    def test_equal_mul(self):
        s = 'aaa'
        assert 'a' * 3 == s


class TestNotEqual:
    def test_notequal_add(self):
        s = 'Hello, world!'
        assert 'Hello, ' + 'world!' is not s

    def test_notequal_mul(self):
        s = 'aaa'
        assert 'a' * 3 is not s
