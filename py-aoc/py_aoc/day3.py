"""day3 module"""
import os

from typing import List

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/3/input.txt")
)


def get_diag_report(data: str) -> List[int]:
    """Get data"""
    diag_report = [int(diag, base=2) for diag in data.splitlines()]
    return diag_report


def part1(diag_report: List[int]) -> int:
    """Part 1"""
    gamma = 0
    epsillon = 0
    for bit in range(max(diag_report).bit_length()):
        # The list of bits for this bit_length
        bit_list = [diag & (0b1 << bit) for diag in diag_report]
        # find most common occuring bit and add it to gamma
        gamma |= max(bit_list, key=bit_list.count)
    # Create a mask of the max bitlength, to easily bitflip without going neg
    mask = int("1" * max(diag_report).bit_length(), base=2)
    epsillon = ~gamma & (mask)
    return gamma * epsillon


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        diag_report = get_diag_report(infile.read())

    print("Part 1:", part1(diag_report))
