from BogoSort import bogo_sort


def test_sort():
    assert bogo_sort([1, 2, 3, 5, 4], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
