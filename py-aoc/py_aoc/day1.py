"""day1 module"""
from itertools import permutations
import os

from typing import List

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/1/input.txt")
)


def get_data_depths(data: str) -> List[int]:
    """Get data for depths"""
    depths = [int(line) for line in data.splitlines()]
    return depths


def part1(depths: List[int]) -> int:
    count = 0
    previous = None
    for current in depths:
        if not previous:
            previous = current
            continue
        if current > previous:
            count += 1
        previous = current
    return count


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        depths = get_data_depths(infile.read())

    print("Part1: ", part1(depths))
