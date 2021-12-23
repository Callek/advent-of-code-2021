"""Tests for day 13"""
from py_aoc import day13


EXAMPLE_DATA = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def test_data_extract() -> None:
    """Test Extract Data"""
    grid, folds = day13.get_grid_and_fold_instructions(EXAMPLE_DATA)
    assert all(isinstance(p, tuple) for p in grid)
    assert all(isinstance(i, int) for p in grid for i in p)
    assert all(isinstance(f[0], str) for f in folds)
    assert all(isinstance(f[1], int) for f in folds)


def test_part1() -> None:
    """Test Part 1"""
    grid, folds = day13.get_grid_and_fold_instructions(EXAMPLE_DATA)
    assert day13.part1(grid, folds) == 17
