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
    ),
)
def test_part1(days: int, expect: int) -> None:
    """Test point data"""
    data = day6.get_initial_fish_age(EXAMPLE_DATA)
    assert day6.part1(data, days) == expect
