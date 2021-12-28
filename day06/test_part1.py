import pytest

from part1 import single_fish
from part1 import calc_fishes


@pytest.mark.parametrize("value, expected",
                         [
                             (8, 7),
                             (0, 6),
                             (1, 0),
                          ]
                         )
def test__single_fish(value, expected):
    result = single_fish(value)
    assert result == expected

@pytest.mark.parametrize("value, expected",
                         [
                             ([0], [6, 8]),
                             ([0, 1, 2], [6,0,1,8]),
                             ([1, 0, 2, 0, 3], [0, 6, 1, 6, 2, 8, 8]),
                             ([0, 1, 0, 5, 6, 7, 8], [6, 0, 6, 4, 5, 6, 7, 8, 8])
                          ]
                         )
def test___calc_fishes(value, expected):
    result = calc_fishes(value)
    assert result == expected
