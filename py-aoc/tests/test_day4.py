"""Tests for day 3"""
from py_aoc import day4


EXAMPLE_DATA = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

expected_calls = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]


def test_data_extract() -> None:
    """Test data extraction"""
    calls, cards = day4.get_calls_and_cards(EXAMPLE_DATA)
    assert all(isinstance(call, int) for call in calls)
    assert calls == expected_calls
    assert all(isinstance(card, day4.Card) for card in cards)
    assert all(isinstance(cell, int) for card in cards for cell in card.cells)


def test_part1_example_mid() -> None:
    """Test stages of example"""
    calls, cards = day4.get_calls_and_cards(EXAMPLE_DATA)
    for call in calls[0:5]:
        day4.call_number(call, cards)
    assert not any(card.is_winner() for card in cards)
    for call in calls[5:11]:
        day4.call_number(call, cards)
    assert not any(card.is_winner() for card in cards)
    day4.call_number(calls[11], cards)
    assert calls[11] == 24
    assert any(card.is_winner() for card in cards)
    assert cards[2].is_winner()
    assert sum(cards[2].unmarked_numbers()) == 188


def test_part1() -> None:
    """Test part 1"""
    calls, cards = day4.get_calls_and_cards(EXAMPLE_DATA)
    magic_num = day4.part1(calls, cards)
    assert magic_num == 4512


def test_part2() -> None:
    """Test part 2"""
    calls, cards = day4.get_calls_and_cards(EXAMPLE_DATA)
    magic_num = day4.part2(calls, cards)
    assert magic_num == 1924
