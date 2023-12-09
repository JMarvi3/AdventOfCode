from collections import deque, defaultdict

from current_puzzle import current_puzzle
import regex as re

puzzle = current_puzzle()
input_data = puzzle.input_data

# input_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

total = 0
cards = dict()
for card in input_data.splitlines():
    card, numbers = card.split(': ')
    card_number = int(card[5:])
    winning, yours = numbers.split(' | ')
    winning = set(map(int,re.findall(r"\d+", winning)))
    yours = set(map(int,re.findall(r"\d+", yours)))
    count = len(yours.intersection(winning))
    if count:
        total += 2**(count-1)
    cards[card_number] = count

puzzle.answer_a = total
print('Part1:', puzzle.answer_a)

max_card = card_number
num_cards = [1 for card in cards]
for card, count in cards.items():
    for new_card in range(card, min(card + count, max_card)):
        num_cards[new_card] += num_cards[card-1]


puzzle.answer_b = sum(num_cards)
print('Part2:', puzzle.answer_b)
