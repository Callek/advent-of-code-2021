"""Tests for day 6"""
from py_aoc import day6

from pytest import mark


EXAMPLE_DATA = """3,4,3,1,2
"""


@mark.parametrize(
    "days,expect",
    (
        [18, 26],
        [80, 5934],
        [256, 26984457539],
    ),
)
def test_spawn(days: int, expect: int) -> None:
    """Test point data"""
    data = day6.get_initial_fish_age(EXAMPLE_DATA)
    assert day6.spawn(data, days) == expect
