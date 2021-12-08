"""day8 module"""
import os

from typing import Dict, List

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/8/input.txt")
)


class Display:
    """Display 7-segment"""

    display_raw: List[str]
    output_raw: List[str]
    number_map: Dict[int, str]

    def __init__(self, raw_data: str) -> None:
        display_data, output_data = raw_data.split("|")
        self.display_raw = ["".join(sorted(d)) for d in display_data.strip().split(" ")]
        self.output_raw = ["".join(sorted(d)) for d in output_data.strip().split(" ")]
        self.number_map = {}
        self.solve_number_map()

    def solve_number_map(self) -> None:
        """Solve the numeric map"""
        self.number_map[1] = next(d for d in self.display_raw if len(d) == 2)
        self.number_map[7] = next(d for d in self.display_raw if len(d) == 3)
        self.number_map[4] = next(d for d in self.display_raw if len(d) == 4)
        self.number_map[8] = next(d for d in self.display_raw if len(d) == 7)


def get_display_data(data: str) -> List[Display]:
    """Get the initial list of fish ages"""
    return [Display(line) for line in data.splitlines()]


def part1(displays: List[Display]) -> int:
    """Part 1"""
    total = sum(
        [
            display.output_raw.count(display.number_map[n])
            for display in displays
            for n in {1, 4, 7, 8}
        ]
    )
    return total


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        displays = get_display_data(infile.read())

    print("Part 1:", part1(displays))
    # print("Part 2:", part2(positions))
