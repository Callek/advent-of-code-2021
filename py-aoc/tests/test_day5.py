"""Tests for day 5"""
from py_aoc import day5

from pytest import mark


EXAMPLE_DATA = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


@mark.parametrize(
    "data,expect",
    (
        ["12,6", day5.Point(12, 6)],
        ["896,7", day5.Point(896, 7)],
        ["999,999", day5.Point(999, 999)],
    ),
)
def test_point(data: str, expect: day5.Point) -> None:
    """Test point data"""
    point = day5.Point.from_data(data)
    assert point == expect


@mark.parametrize(
    "data,expect,angled",
    (
        ["0,9 -> 5,9", day5.Line(day5.Point(0, 9), day5.Point(5, 9)), False],
        ["9,4 -> 3,4", day5.Line(day5.Point(9, 4), day5.Point(3, 4)), False],
        ["6,4 -> 2,0", day5.Line(day5.Point(6, 4), day5.Point(2, 0)), True],
    ),
)
def test_line(data: str, expect: day5.Point, angled: bool) -> None:
    """Test line data"""
    line = day5.Line.from_data(data)
    assert line == expect
    assert line.is_angled() == angled


def test_data_extract() -> None:
    """Test data extraction"""
    lines = day5.get_lines(EXAMPLE_DATA)
    assert all(isinstance(line, day5.Line) for line in lines)


def test_part1() -> None:
    """Test part 1"""
    lines = day5.get_lines(EXAMPLE_DATA)
    assert day5.part1(lines) == 5


def test_part2() -> None:
    """Test part 2"""
    lines = day5.get_lines(EXAMPLE_DATA)
    assert day5.part2(lines) == 12
