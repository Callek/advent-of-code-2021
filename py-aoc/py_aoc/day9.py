"""day9 module"""
import os

from typing import Callable, List

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/9/input.txt")
)


def get_heightmap(data: str) -> List[str]:
    return data.splitlines()


def part1(heightmap: List[str]) -> int:
    risk_sum = 0
    for row, heights in enumerate(heightmap):
        for column, height in enumerate(heights):
            check_left: Callable[[], bool] = lambda: True
            check_right: Callable[[], bool] = lambda: True
            check_up: Callable[[], bool] = lambda: True
            check_down: Callable[[], bool] = lambda: True
            if not column == 0:
                check_left = lambda: heights[column - 1] > height
            if not (column + 1) == len(heights):
                check_right = lambda: heights[column + 1] > height
            if not row == 0:
                check_up = lambda: heightmap[row - 1][column] > height
            if not (row + 1) == len(heightmap):
                check_down = lambda: heightmap[row + 1][column] > height
            if check_up() and check_down() and check_left() and check_right():
                risk_sum += int(height) + 1
    return risk_sum


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        heightmap = get_heightmap(infile.read())

    print("Part 1:", part1(heightmap))
    # print("Part 2:", part2(heightmap))
