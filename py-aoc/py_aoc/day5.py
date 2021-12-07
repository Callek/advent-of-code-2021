"""day5 module"""
import os

from typing import Any, List

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/5/input.txt")
)


class Point:
    """A single point"""

    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_data(cls, data: str) -> "Point":
        """Parse a Point from data"""
        x, y = (int(p) for p in data.strip().split(","))
        return Point(x, y)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Point<{self.x}, {self.y}>"


class Line:
    """Represent a line"""

    start: Point
    end: Point

    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    @classmethod
    def from_data(cls, data: str) -> "Line":
        """Parse a Line from data"""
        start_data, end_data = (edge for edge in data.strip().split("->"))
        start = Point.from_data(start_data)
        end = Point.from_data(end_data)
        return Line(start, end)

    def is_angled(self) -> bool:
        """Returns False if this line is vertical or horizontal"""
        if self.start.x == self.end.x or self.start.y == self.end.y:
            return False
        return True

    def max_x(self) -> int:
        """Return the max x coord"""
        return max(self.start.x, self.end.x)

    def max_y(self) -> int:
        """Return the max y coord"""
        return max(self.start.y, self.end.y)

    def walk(self) -> List[Point]:
        """Returns a list of points along the line

        Assumes horizontal/vertical"""
        walking = []
        step_x = 0
        step_y = 0
        if self.start.x > self.end.x:
            step_x = -1
        if self.start.x < self.end.x:
            step_x = 1
        if self.start.y > self.end.y:
            step_y = -1
        if self.start.y < self.end.y:
            step_y = 1
        if not step_y == 0:
            y_walk = list(range(self.start.y, self.end.y + step_y, step_y))
        if not step_x == 0:
            x_walk = list(range(self.start.x, self.end.x + step_x, step_x))
        if step_x == 0:
            x_walk = [self.start.x] * len(y_walk)
        if step_y == 0:
            y_walk = [self.start.y] * len(x_walk)
        for x, y in zip(x_walk, y_walk):
            walking.append(Point(x, y))
        return walking

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Line):
            return False
        return self.start == other.start and self.end == other.end

    def __repr__(self) -> str:
        return f"Line<start={self.start}, end={self.end}>"


def get_lines(data: str) -> List[Line]:
    """Parse data to get the number of Lines"""
    lines: List[Line] = []
    for line in data.splitlines():
        lines.append(Line.from_data(line))
    return lines


def part1(lines: List[Line]) -> int:
    """Compute Part 1"""
    max_x = max(line.max_x() for line in lines)
    max_y = max(line.max_y() for line in lines)
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Mark the grid
    for line in lines:
        if line.is_angled():
            continue
        for point in line.walk():
            grid[point.y][point.x] += 1
    total = sum(sum(coord >= 2 for coord in l) for l in grid)
    return total


def part2(lines: List[Line]) -> int:
    """Compute Part 2"""
    max_x = max(line.max_x() for line in lines)
    max_y = max(line.max_y() for line in lines)
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Mark the grid
    for line in lines:
        for point in line.walk():
            grid[point.y][point.x] += 1
    total = sum(sum(coord >= 2 for coord in l) for l in grid)
    return total


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        lines = get_lines(infile.read())

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
