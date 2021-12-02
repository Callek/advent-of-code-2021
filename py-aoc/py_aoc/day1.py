"""day1 module"""
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
    """Part1"""
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


def part2(depths: List[int]) -> int:
    """Part2"""
    min_slice = 0
    max_slice = 3
    count = 0
    while max_slice <= len(depths):
        previous_depths = depths[min_slice:max_slice]
        current_depths = depths[min_slice + 1 : max_slice + 1]
        if sum(current_depths) > sum(previous_depths):
            count += 1
        min_slice += 1
        max_slice += 1
    return count


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        depths = get_data_depths(infile.read())

    print("Part1: ", part1(depths))
    print("Part2: ", part2(depths))
