import re
import itertools
from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

pat = re.compile(r'(\w+): \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+)')
names, facts, cals = [], [], []
for line in input_data.splitlines():
    name, cap, dur, flav, text, cal = pat.match(line).groups()
    names.append(name)
    facts.append((int(cap), int(dur), int(flav), int(text)))
    cals.append(int(cal))

all_recipes = itertools.combinations_with_replacement(names, 100)

best_score, best_amounts = 0, []
best_cal, best_cal_amounts = 0, []
for recipe in all_recipes:
    scores = [0, 0, 0, 0]
    amounts = []
    calories = 0
    for i in range(len(names)):
        count = recipe.count(names[i])
        amounts.append(count)
        for ing in range(4):
            scores[ing] += facts[i][ing] * count
        calories += cals[i] * count
    score = 1
    for ing in range(4):
        score *= max(0, scores[ing])
    if score > best_score:
        best_score = score
        best_amounts = amounts
    best_score = max(best_score, score)
    if calories == 500 and score > best_cal:
        best_cal = score
        best_cal_amounts = amounts

print(names)
puzzle.answer_a = best_score
print('Part1:', puzzle.answer_a, best_amounts)

puzzle.answer_b = best_cal
print('Part2:', puzzle.answer_b, best_cal_amounts)
