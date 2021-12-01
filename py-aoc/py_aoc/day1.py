"""day1 module"""
from itertools import permutations
import os

inputfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../days/1/input.txt"))

def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        data = [int(line) for line in infile]

    data2 = data[:]
    while data2:
        item1 = data2.pop()
        item2 = 0
        for item2 in data2:
            if item1 + item2 == 2020:
                answer = item1 * item2
                print(
                    f"The values '{item1} + {item2} == 2020' therefore the answer is "
                    f"'{item1} * {item2} == {answer}'")

    for item1, item2, item3 in permutations(data, 3):
        if item1 + item2 + item3 == 2020:
            answer = item1 * item2 * item3
            print(
                f"The values '{item1} + {item2} + {item3} == 2020' therefore the answer is "
                f"'{item1} * {item2} * {item3} == {answer}'")
            break
