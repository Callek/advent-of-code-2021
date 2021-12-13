"""day10 module"""
import os

from typing import Dict, Tuple, Set

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/11/input.txt")
)


def get_octopus_grid(data: str) -> Dict[Tuple[int, int], int]:
    """Get the initial grid of octopi"""
    return {
        (x, y): int(val)
        for y, y_axis in enumerate(data.splitlines())
        for x, val in enumerate(y_axis)
    }


def bump_all_energy_level(grid: Dict[Tuple[int, int], int]) -> None:
    """Bump all energy levels - relies on mutability of grid"""
    for k in grid:
        grid[k] += 1


def get_neighbors(
    grid: Dict[Tuple[int, int], int], x: int, y: int
) -> Set[Tuple[int, int]]:
    """Get the neighbors in this grid"""
    return {
        (x + dx, y + dy)
        for (dx, dy) in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )
        if (x + dx, y + dy) in grid
    }


def do_flashing(grid: Dict[Tuple[int, int], int]) -> int:
    """Flash the octopuses and adjacent, resetting the luminosity after complete"""
    flashed: Set[Tuple[int, int]] = set()
    queue: Set[Tuple[int, int]] = {k for k, val in grid.items() if val > 9}
    while queue:
        target = queue.pop()
        x, y = target
        flashed.add(target)
        for neighbor in get_neighbors(grid, x, y):
            if not neighbor in flashed:
                grid[neighbor] += 1
                if grid[neighbor] > 9:
                    queue.add(neighbor)
    for reset in flashed:
        grid[reset] = 0
    return len(flashed)


def part1(grid: Dict[Tuple[int, int], int], steps: int = 100) -> int:
    """Part 1"""
    total_flashed = 0
    for _ in range(steps):
        bump_all_energy_level(grid)
        total_flashed += do_flashing(grid)
    return total_flashed


def part2(grid: Dict[Tuple[int, int], int]) -> int:
    """Part 2"""
    step = 0
    while True:
        bump_all_energy_level(grid)
        step += 1
        if do_flashing(grid) == len(grid):
            break
        if step == 10000:
            break
    return step


def main() -> None:
    """Main Logic"""
    with open(inputfile, mode="r", encoding="utf-8") as infile:
        grid = get_octopus_grid(infile.read())

    print("Part 1:", part1(grid.copy()))
    print("Part 2:", part2(grid.copy()))
