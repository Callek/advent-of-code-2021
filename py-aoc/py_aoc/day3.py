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


def part2(diag_report: List[int]) -> int:
    """Part 2"""
    co2_rating = 0
    o2_rating = 0
    _co2_rating_report = diag_report[:]
    _o2_rating_report = diag_report[:]
    for bit in reversed(range(max(diag_report).bit_length())):
        # Use some magic here, by sorting the list and reversing it, so that we can use the max
        # trick.  Max on an equal split of 0 and 1 will return the first occurance rather than a
        # random
        bit_list_co2 = list(
            reversed(sorted([diag & (0b1 << bit) for diag in _co2_rating_report]))
        )
        bit_list_o2 = list(
            reversed(sorted([diag & (0b1 << bit) for diag in _o2_rating_report]))
        )
        most_present_bit_co2 = max(bit_list_co2, key=bit_list_co2.count)
        most_present_bit_o2 = max(bit_list_o2, key=bit_list_o2.count)
        if len(_o2_rating_report) > 1:
            _o2_rating_report = [
                diag
                for diag in _o2_rating_report
                if ((diag >> bit) & 1) == (most_present_bit_o2 >> bit)
            ]
        if len(_co2_rating_report) > 1:
            _co2_rating_report = [
                diag
                for diag in _co2_rating_report
                if not ((diag >> bit) & 1) == (most_present_bit_co2 >> bit)
            ]
        _co2_rating_report
    co2_rating = _co2_rating_report[0]
    o2_rating = _o2_rating_report[0]

    return co2_rating * o2_rating


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        diag_report = get_diag_report(infile.read())

    print("Part 1:", part1(diag_report))
    print("Part 2:", part2(diag_report))
