"""Tests for day 7"""
from py_aoc import day9


EXAMPLE_DATA = """2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_heightmap_data() -> None:
    """Test data retrieval"""
    heightmap = day9.get_heightmap(EXAMPLE_DATA)
    assert isinstance(heightmap, list)
    assert all(isinstance(h, str) for h in heightmap)


def test_part1() -> None:
    """Test Part 1"""
    data = day9.get_heightmap(EXAMPLE_DATA)
    assert day9.part1(data) == 15


def test_part2() -> None:
    """Test Part 2"""
    data = day9.get_heightmap(EXAMPLE_DATA)
    assert day9.part2(data) == 1134
