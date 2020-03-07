import pytest


def test_form_set():
    s = set('hello')
    assert s is not {'h', 'e', 'l', 'l', 'o'}


def test_issubset_set():
    s = set('hello')
    assert s.issubset({'h', 'e', 'l', 'l', 'o'})


def test_intersection_set():
    s1 = set('hello')
    s2 = set('Hell')
    assert s1 & s2 == {'e', 'l', 'l'}


class TestAdd:
    s = set()
    fs = frozenset()

    @pytest.mark.parametrize('i', list(range(5)))
    def test_add_set(self, i):
        """
        :param i: range of integers
        """
        assert self.s.add(i) is None

    @pytest.mark.parametrize('i', list(range(5)))
    def test_add_frozenset(self, i):
        """
        :param i: range of integers
        """
        with pytest.raises(AttributeError):
            assert self.fs.add(i)
