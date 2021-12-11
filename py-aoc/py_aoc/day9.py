"""day9 module"""
import math
import os

from typing import Callable, Dict, List, Tuple, Set

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/9/input.txt")
)


def get_heightmap(data: str) -> List[str]:
    """Get the heightmap data"""
    return data.splitlines()


def part1(heightmap: List[str]) -> int:
    """Part 1"""
    risk_sum = 0
    for row, heights in enumerate(heightmap):
        for column, height in enumerate(heights):
            check_left: Callable[[], bool] = lambda: True
            check_right: Callable[[], bool] = lambda: True
            check_up: Callable[[], bool] = lambda: True
            check_down: Callable[[], bool] = lambda: True
            if not column == 0:
                check_left = lambda: heights[column - 1] > height
            if not (column + 1) == len(heights):
                check_right = lambda: heights[column + 1] > height
            if not row == 0:
                check_up = lambda: heightmap[row - 1][column] > height
            if not (row + 1) == len(heightmap):
                check_down = lambda: heightmap[row + 1][column] > height
            if check_up() and check_down() and check_left() and check_right():
                risk_sum += int(height) + 1
    return risk_sum


def find_neighbors(
    heightmap: Dict[Tuple[int, int], int], x: int, y: int
) -> List[Tuple[int, int]]:
    """Neighbor coords of a given point"""
    neighbors = [
        (x + dx, y + dy)
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1))
        if ((x + dx), (y + dy)) in heightmap
    ]
    return neighbors


def find_neighbor_values(
    heightmap: Dict[Tuple[int, int], int], x: int, y: int
) -> List[int]:
    """Neighbor values of a given point"""
    return [heightmap[(x2, y2)] for (x2, y2) in find_neighbors(heightmap, x, y)]


def find_low_points(heightmap: Dict[Tuple[int, int], int]) -> List[Tuple[int, int]]:
    """Low Points"""
    low_points = []
    for (x, y) in heightmap:
        if heightmap[(x, y)] < min(find_neighbor_values(heightmap, x, y)):
            low_points.append((x, y))
    return low_points


def breadth_search(
    heightmap: Dict[Tuple[int, int], int],
    visited: Set[Tuple[int, int]],
    init_coord: Tuple[int, int],
) -> Tuple[int, Set[Tuple[int, int]]]:
    """Search by breadth"""
    queue = [init_coord]
    visited.add(init_coord)
    count = 0
    while queue:
        x, y = queue.pop()
        count += 1
        for neighbor in find_neighbors(heightmap, x, y):
            if heightmap[neighbor] == 9 or heightmap[neighbor] <= heightmap[(x, y)]:
                continue
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return count, visited


def part2(data: List[str]) -> int:
    """Part 2"""
    heightmap = {
        (x, y): int(height)
        for y, line in enumerate(data)
        for x, height in enumerate(line)
    }
    visited: Set[Tuple[int, int]] = set()
    basin_sizes = []
    low_points = find_low_points(heightmap)
    for coord in low_points:
        if coord in visited:
            continue
        basin_size, visited = breadth_search(heightmap, visited, coord)
        basin_sizes.append(basin_size)
    return math.prod(sorted(basin_sizes)[-3:])


def main() -> None:
    """Main Logic"""
    with open(inputfile, mode="r", encoding="utf-8") as infile:
        heightmap = get_heightmap(infile.read())

    print("Part 1:", part1(heightmap))
    print("Part 2:", part2(heightmap))
