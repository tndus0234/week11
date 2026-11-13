from bug3_logic import find_max


def test_maximum_is_first():
    assert find_max([9, 5, 2]) == 9


def test_maximum_is_in_middle():
    assert find_max([1, 9, 2]) == 9


def test_maximum_is_last():
    assert find_max([1, 2, 9]) == 9