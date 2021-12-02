"""Tests for day 1"""
from py_aoc import day1


EXAMPLE_DATA = """199
200
208
210
200
207
240
269
260
263
"""


def test_nums() -> None:
    """Test data extraction"""
    assert all(isinstance(x, int) for x in day1.get_data_depths(EXAMPLE_DATA))


def test_num_increasing() -> None:
    """Test part 1"""
    depths = day1.get_data_depths(EXAMPLE_DATA)

    assert day1.part1(depths) == 7


def test_sliding_window() -> None:
    """Test part 2"""
    depths = day1.get_data_depths(EXAMPLE_DATA)

    assert day1.part2(depths) == 5
