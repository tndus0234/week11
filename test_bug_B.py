from bug3_logic import find_max


def test_maximum_is_first():
    assert find_max([9, 5, 2]) == 9


def test_maximum_is_in_middle():
    assert find_max([1, 9, 2]) == 9


def test_maximum_is_last():
    assert find_max([1, 2, 9]) == 9


def test_single_item():
    assert find_max([7]) == 7


def test_negative_numbers():
    assert find_max([-5, -2, -8]) == -2
