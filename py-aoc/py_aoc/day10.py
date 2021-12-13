"""day10 module"""
import os
import statistics

from typing import List

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/10/input.txt")
)


def get_nav_data(data: str) -> List[str]:
    """Get the initial list of fish ages"""
    return data.splitlines()


def calc_part1_error_line(nav_sequence: str) -> int:
    """Calculate the error value for this line in Part 1"""
    OPEN_MAP = ("(", "{", "[", "<")
    CLOSING_MAP = (")", "}", "]", ">")
    INVALID_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
    expect_closing = []
    for char in nav_sequence:
        if char in OPEN_MAP:
            expect_closing.append(CLOSING_MAP[OPEN_MAP.index(char)])
        elif expect_closing and char == expect_closing[-1]:
            expect_closing.pop()
        else:
            # Invalid
            return INVALID_SCORE[char]
    return 0


def part1(nav: List[str]) -> int:
    """Part 1"""
    error_score = 0
    for nav_sequence in nav:
        error_score += calc_part1_error_line(nav_sequence)
    return error_score


def tokenize_expected_closing(nav_sequence: List[str]) -> List[str]:
    """Calculate the closing token list for Part 2"""
    OPEN_MAP = ("(", "{", "[", "<")
    CLOSING_MAP = (")", "}", "]", ">")
    expect_closing = []
    for char in nav_sequence:
        if char in OPEN_MAP:
            expect_closing.append(CLOSING_MAP[OPEN_MAP.index(char)])
        elif expect_closing and char == expect_closing[-1]:
            expect_closing.pop()
    return expect_closing


def part2(nav: List[str]) -> int:
    """Part 2"""
    total_scores = []
    COMPLETION_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}
    for nav_sequence in nav:
        line_score = 0
        if calc_part1_error_line(nav_sequence):
            # Has an error, skip this line
            continue
        tokens = tokenize_expected_closing(nav_sequence)
        while tokens:
            line_score *= 5
            line_score += COMPLETION_SCORE[tokens.pop()]
        total_scores.append(line_score)

    return statistics.median(total_scores)


def main() -> None:
    """Main Logic"""
    with open(inputfile, mode="r", encoding="utf-8") as infile:
        nav = get_nav_data(infile.read())

    print("Part 1:", part1(nav))
    print("Part 2:", part2(nav))
