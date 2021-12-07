"""day7 module"""
import math
import os
import statistics

from typing import List

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/7/input.txt")
)


def get_crab_pos(data: str) -> List[int]:
    """Get the initial list of fish ages"""
    return [int(pos) for pos in data.split(",")]


def part1(crab_pos: List[int]) -> int:
    """Part 1"""
    med = statistics.median(crab_pos)
    return sum(abs(med - pos) for pos in crab_pos)


def part2(crab_pos: List[int]) -> int:
    """Part 2"""
    mean = statistics.mean(crab_pos)
    mean_ceil = math.ceil(mean)
    mean_floor = math.floor(mean)
    fuel_ceil = sum(
        abs(mean_ceil - i) * (abs(mean_ceil - i) + 1) // 2 for i in crab_pos
    )
    fuel_floor = sum(
        abs(mean_floor - i) * (abs(mean_floor - i) + 1) // 2 for i in crab_pos
    )
    return min(fuel_ceil, fuel_floor)


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        positions = get_crab_pos(infile.read())

    print("Part 1:", part1(positions))
    print("Part 2:", part2(positions))
