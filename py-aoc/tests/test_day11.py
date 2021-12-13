"""Tests for day 5"""
from py_aoc import day11

from pytest import mark


EXAMPLE_DATA = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


@mark.parametrize(
    "steps,expect",
    (
        [1, 0],
        [2, 35],
        [10, 204],
        [100, 1656],
    ),
)
def test_part1(steps: int, expect: int) -> None:
    """Test part 1"""
    grid = day11.get_octopus_grid(EXAMPLE_DATA)
    assert day11.part1(grid, steps) == expect


def test_part2() -> None:
    grid = day11.get_octopus_grid(EXAMPLE_DATA)
    assert day11.part2(grid) == 195
