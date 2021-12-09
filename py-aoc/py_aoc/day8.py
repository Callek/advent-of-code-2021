"""day8 module"""
import math
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
        self.number_map[6] = next(
            d
            for d in self.display_raw
            if len(d) == 6 and not set(d).issuperset(set(self.number_map[7]))
        )
        top_right_seg = "".join(
            set(self.number_map[7]).difference(set(self.number_map[6]))
        )
        bottom_right_seg = "".join(
            set(self.number_map[1]).difference(set(top_right_seg))
        )
        self.number_map[5] = next(
            d for d in self.display_raw if len(d) == 5 and top_right_seg not in d
        )
        self.number_map[2] = next(
            d for d in self.display_raw if bottom_right_seg not in d
        )
        bottom_left_seg = "".join(set(self.number_map[6]) - set(self.number_map[5]))
        self.number_map[3] = "".join(
            d
            for d in self.display_raw
            if len(d) == 5 and d not in self.number_map.values()
        )
        self.number_map[0] = "".join(
            d
            for d in self.display_raw
            if len(d) == 6
            and d not in self.number_map.values()
            and bottom_left_seg in d
        )
        self.number_map[9] = "".join(
            d for d in self.display_raw if d not in self.number_map.values()
        )

    def get_number_by_value(self, value: str) -> int:
        return next(k for k, v in self.number_map.items() if v == value)

    def get_output_number(self) -> int:
        num = 0
        for i, d in enumerate(self.output_raw):
            num += self.get_number_by_value(d) * int(math.pow(10, 3 - i))
        return num


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


def part2(displays: List[Display]) -> int:
    """Part 2"""
    return sum(d.get_output_number() for d in displays)


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        displays = get_display_data(infile.read())

    print("Part 1:", part1(displays))
    print("Part 2:", part2(displays))
