"""Tests for day 7"""
from py_aoc import day7


EXAMPLE_DATA = """16,1,2,0,4,2,7,1,2,14
"""


def test_part1() -> None:
    """Test point data"""
    data = day7.get_crab_pos(EXAMPLE_DATA)
    assert day7.part1(data) == 37


def test_part2() -> None:
    """Test point data"""
    data = day7.get_crab_pos(EXAMPLE_DATA)
    assert day7.part2(data) == 168
