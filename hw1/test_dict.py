import pytest


class TestForm:
    formed_d = {'python': None, 'c++': None}

    def test_form_fromkeys(self):
        d = dict.fromkeys(['python', 'c++'])
        assert d == self.formed_d

    def test_form_add(self):
        keys = ['python', 'c++']
        d = dict()
        for _ in keys:
            d[_] = None
        assert d == self.formed_d


def test_copy_dict():
    d = {'python': [3.8, 3.7, 3.6], 'c++': [17, 14, 11]}
    assert d.copy() == d


@pytest.mark.parametrize('i', ['java', 'php'])
def test_get_key(i):
    """
    :param i: list of string
    """
    d = {'python': [3.8, 3.7, 3.6], 'c++': [17, 14, 11]}
    assert d.get(i) is None


@pytest.mark.parametrize('i', ['java', 'php'])
def test_pop_key(i):
    """
    :param i: list of string
    """
    d = {'python': [3.8, 3.7, 3.6], 'c++': [17, 14, 11]}
    with pytest.raises(KeyError):
        assert d.pop(i)
