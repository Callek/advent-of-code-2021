"""day6 module"""
import os

from typing import List

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/6/input.txt")
)


def get_initial_fish_age(data: str) -> List[int]:
    """Get the initial list of fish ages"""
    return [int(age) for age in data.split(",")]


def spawn(fish_ages: List[int], days: int) -> int:
    """Spawn"""
    MAX_AGE = 8
    NEW_SPAWN_AGE = 8
    SPAWN_RESET_AGE = 6
    groups: List[int] = [0] * (MAX_AGE + 1)  # Indexed by age left
    for i in range(MAX_AGE + 1):
        groups[i] = fish_ages.count(i)

    for _ in range(days):
        spawning = groups[0]
        for i in range(1, MAX_AGE + 1):
            groups[i - 1] = groups[i]
        groups[MAX_AGE] = 0
        groups[NEW_SPAWN_AGE] += spawning
        groups[SPAWN_RESET_AGE] += spawning
    return sum(groups)


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        ages = get_initial_fish_age(infile.read())

    print("Part 1:", spawn(ages, 80))
    print("Part 2:", spawn(ages, 256))
