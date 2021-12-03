"""Tests for day 3"""
from py_aoc import day3


EXAMPLE_DATA = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def test_data_extract() -> None:
    """Test data extraction"""
    diag_report = day3.get_diag_report(EXAMPLE_DATA)
    assert all(isinstance(diag, int) for diag in diag_report)
    expected_ints = [4, 30, 22, 23, 21, 15, 7, 28, 16, 25, 2, 10]
    assert diag_report == expected_ints


def test_part1() -> None:
    """Test part 1"""
    diag_report = day3.get_diag_report(EXAMPLE_DATA)
    assert day3.part1(diag_report) == 198


def test_part2() -> None:
    """Test part 2"""
    diag_report = day3.get_diag_report(EXAMPLE_DATA)
    assert day3.part2(diag_report) == 230
