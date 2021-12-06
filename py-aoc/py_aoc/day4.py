"""day4 module"""
import os

from typing import List, Tuple

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../days/4/input.txt")
)


class Card:
    """A bingo card"""

    cells: List[int] = []
    marked: List[bool] = []
    _winner: bool = False

    def __init__(self, card_data: str) -> None:
        """Init the bingo card"""
        self.cells = [int(cell) for cell in card_data.split()]
        self.marked = [False for _ in range(len(self.cells))]

    def mark(self, call: int) -> bool:
        """Marks this card

        Returns True if this wins
        """
        if call not in self.cells:
            return False
        index = self.cells.index(call)
        self.marked[index] = True
        return self.is_winner()

    def unmarked_numbers(self) -> List[int]:
        """Get list of unmarked numbers"""
        return [
            self.cells[index]
            for index in range(len(self.cells))
            if self.marked[index] is False
        ]

    def is_winner(self) -> bool:
        """Did this card win.

        Caches winning or not"""
        if self._winner:
            return True

        if (
            # Horizontal Win
            all(self.marked[0:5])
            or all(self.marked[5:10])
            or all(self.marked[10:15])
            or all(self.marked[15:20])
            or all(self.marked[20:25])
            # Vertical Win
            or all(self.marked[0:25:5])
            or all(self.marked[1:25:5])
            or all(self.marked[2:25:5])
            or all(self.marked[3:25:5])
            or all(self.marked[4:25:5])
            # Diag Win
            # or all(self.marked[0:25:6])
            # or all(self.marked[4:25:4])
        ):
            self._winner = True
        return self._winner


def get_bingo_calls(data: str) -> List[int]:
    """Get calls"""
    calls = [int(call) for call in data.split(",")]
    return calls


def get_bingo_cards(data: List[str]) -> List[Card]:
    """Get bingo cards from data"""
    cards = []
    for card_data in data:
        cards.append(Card(card_data))
    return cards


def get_calls_and_cards(data: str) -> Tuple[List[int], List[Card]]:
    """Get bingo calls and cards from input data"""
    split_data = data.split("\n\n")
    calls = get_bingo_calls(split_data[0])
    cards = get_bingo_cards(split_data[1:])
    return calls, cards


def call_number(call: int, cards: List[Card]) -> None:
    """Call a number"""
    for card in cards:
        card.mark(call)


def part1(calls: List[int], cards: List[Card]) -> int:
    """Part 1"""
    for call in calls:
        call_number(call, cards)
        if not any(card.is_winner() for card in cards):
            continue
        for card in cards:
            if card.is_winner():
                return call * sum(card.unmarked_numbers())
    return 0


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        calls, cards = get_calls_and_cards(infile.read())

    print("Part 1:", part1(calls, cards))
    # print("Part 2:", part2(diag_report))
