import pytest


def test_len_list():
    lst = [0, 1, 2, 3, 4, 5]
    assert len(lst) == 6


@pytest.mark.parametrize('i', [0, 1, 2, 3, 4, 5])
def test_empty_list(i):
    """
    :param i: list of integers
    """
    lst = [0, 1, 2, 3, 4, 5]
    lst.remove(i)
    with pytest.raises(ValueError):
        assert lst.index(i)


def test_clear_list():
    lst = [0, 1, 2, 3, 4, 5]
    assert not lst.clear()


class TestReverse:
    def init(self):
        self.lst = [0, 1, 2, 3, 4, 5]
        self.r_lst = [5, 4, 3, 2, 1, 0]

    def test_reverse_slice(self):
        self.init()
        assert self.lst[::-1] == self.r_lst

    def test_reverse_list(self):
        self.init()
        self.lst.reverse()
        assert self.lst == self.r_lst

    def test_reverse_sort(self):
        self.init()
        self.lst.sort(reverse=True)
        assert self.lst == self.r_lst
