"""day10 module"""
import os

from typing import Dict, Generator, List

# pylint: disable=invalid-name
inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/12/input.txt")
)


def get_path_segments(data: str) -> Dict[str, List[str]]:
    """Gets the graph segments for a given input"""
    graph: Dict[str, List[str]] = {}
    for line in data.splitlines():
        if not line:
            continue
        seg1, seg2 = line.strip().split("-")
        graph.setdefault(seg1, []).append(seg2)
        graph.setdefault(seg2, []).append(seg1)
    return graph


def count_paths(
    all_segments: Dict[str, List[str]], node: str, current_path: List[str]
) -> Generator[int, None, None]:
    """Count all possible paths from node to 'end'"""
    current_path.append(node)
    for n in all_segments[node]:
        if n == "end":
            yield 1
        elif n.isupper() or n not in current_path:
            yield from count_paths(all_segments, n, current_path)
    current_path.pop()


def part1(segments: Dict[str, List[str]]) -> int:
    """Part 1"""
    return sum(count_paths(segments, "start", []))


def main() -> None:
    """Main Logic"""
    with open(inputfile, mode="r", encoding="utf-8") as infile:
        segments = get_path_segments(infile.read())

    print("Part 1:", part1(segments.copy()))
    # print("Part 2:", part2(grid.copy()))
