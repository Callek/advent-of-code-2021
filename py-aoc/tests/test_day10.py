"""Tests for day 10"""
from py_aoc import day10


EXAMPLE_DATA = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def test_nav_data() -> None:
    """Test data retrieval"""
    nav = day10.get_nav_data(EXAMPLE_DATA)
    assert isinstance(nav, list)
    assert all(isinstance(n, str) for n in nav)


def test_part1() -> None:
    """Test Part 1"""
    data = day10.get_nav_data(EXAMPLE_DATA)
    assert day10.part1(data) == 26397


def test_part2() -> None:
    """Test Part 2"""
    data = day10.get_nav_data(EXAMPLE_DATA)
    assert day10.part2(data) == 288957
