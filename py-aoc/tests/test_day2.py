"""Tests for day 2"""
from py_aoc import day2


EXAMPLE_DATA = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def test_data_extract() -> None:
    """Test data extraction"""
    commands = day2.get_data_commands(EXAMPLE_DATA)
    assert all(isinstance(cmd[1], int) for cmd in commands)
    assert all(isinstance(cmd[0], str) for cmd in commands)


def test_part1() -> None:
    """Test part1"""
    commands = day2.get_data_commands(EXAMPLE_DATA)

    assert day2.part1(commands) == 150
