import pytest
import random


@pytest.mark.parametrize('i', list(range(5)))
def test_is_int(i):
    """
    :param i: range of integers
    """
    assert type(i).__name__ == 'int'


def test_notequal_int():
    assert random.randint(0, 10000) != random.randint(0, 10000)


class TestDiv:
    def test_div_zero(self):
        with pytest.raises(ZeroDivisionError):
            assert 1 / 0

    @pytest.mark.parametrize('i', list(range(1, 5)))
    def test_div_int(self, i):
        """
        :param i: range of integers
        """
        assert i // i == 1

    def test_div_mod(self):
        assert 2 % 2 == 0
