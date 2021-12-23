"""day13 module"""
import os

from typing import List, Set, Tuple

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/13/input.txt")
)

POINTS_MYPY = Set[Tuple[int, int]]
FOLD_MYPY = Tuple[str, int]


def get_grid_and_fold_instructions(data: str) -> Tuple[POINTS_MYPY, List[FOLD_MYPY]]:
    """Parse data"""
    dots_raw, fold_raw = data.split("\n\n")
    points = set()
    folds = []
    for point in dots_raw.splitlines():
        x, y = point.split(",")
        points.add((int(x), int(y)))
    for fold in fold_raw.splitlines():
        axis, coord = fold.replace("fold along ", "").split("=")
        folds.append((axis, int(coord)))
    return points, folds


def fold_grid(points: POINTS_MYPY, fold: FOLD_MYPY) -> POINTS_MYPY:
    """Fold the grid once"""
    new_points = set()
    fold_y = fold[0] == "y"
    fold_int = fold[1]
    for x, y in points:
        if fold_y and y > fold_int:
            new_points.add((x, fold_int - (y - fold_int)))
        elif not fold_y and x > fold_int:
            new_points.add((fold_int - (x - fold_int), y))
        else:
            new_points.add((x, y))
    return new_points


def part1(points: POINTS_MYPY, folds: List[FOLD_MYPY]) -> int:
    """Part 1"""
    return len(fold_grid(points, folds[0]))


def part2(points: POINTS_MYPY, folds: List[FOLD_MYPY]) -> str:
    """Part 2"""
    result = "\n"
    grid = points.copy()
    for fold in folds:
        grid = fold_grid(grid, fold)
    for y in range(max(y for _, y in grid) + 1):
        for x in range(max(x for x, _ in grid) + 1):
            if (x, y) in grid:
                result += "#"
            else:
                result += "."
        result += "\n"
    return result


def main() -> None:
    """Main Logic"""
    with open(inputfile, mode="r", encoding="utf-8") as infile:
        grid, folds = get_grid_and_fold_instructions(infile.read())

    print("Part 1:", part1(grid, folds))

    print("Part 2:", part2(grid, folds))
