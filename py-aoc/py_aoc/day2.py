"""day2 module"""
import os

from typing import List, Tuple

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/2/input.txt")
)


def get_data_commands(data: str) -> List[Tuple[str, int]]:
    """Parse Data"""
    commands = [
        (cmd, int(mag))
        for full_command in data.splitlines()
        for (cmd, mag) in [full_command.split()]
    ]
    return commands


def part1(commands: List[Tuple[str, int]]) -> int:
    """part1"""
    horizontal = 0
    vertical = 0
    for cmd in commands:
        if cmd[0] == "forward":
            horizontal += cmd[1]
        if cmd[0] == "up":
            vertical -= cmd[1]
        if cmd[0] == "down":
            vertical += cmd[1]
    return horizontal * vertical


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        commands = get_data_commands(infile.read())

    print("Part1: ", part1(commands))
