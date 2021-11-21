from collections import Counter
from parse import compile, with_pattern
from current_puzzle import current_puzzle
from copy import deepcopy
import time

debug = False


def log(s):
    if debug:
        print(s)


def unit_total(groups):
    return sum(group['units'] for group in groups)


def damage(attacker, defender):
    if attacker['type'] in defender['modifier']['immune']:
        base = 0
    else:
        base = attacker['damage'] * attacker['units']
        if attacker['type'] in defender['modifier']['weak']:
            base *= 2
    return base


@with_pattern(r"(\(.*\) )?")
def parse_modifier(text):
    modifiers = {'weak': {}, 'immune': {}}
    if text:
        for mod in text[1:-2].split('; '):
            mod_split = mod.split(' to ')
            modifiers[mod_split[0]] = set(mod_split[1].split(', '))
    return modifiers


def simulate(groups, boost=0):
    groups = deepcopy(groups)
    for group in groups:
        if group['group_type'] == 'Immune System':
            group['damage'] += boost
    while True:
        damage_done = False
        log(f"Start of round: {len(groups)}, {unit_total(groups)}")
        choices = []
        targeted = set()
        groups.sort(key=lambda g: (-g['units'] * g['damage'], -g['initiative']))
        for i, attacker in enumerate(groups):
            targets = [target for target in groups if target['id'] not in targeted and
                       target['group_type'] != attacker['group_type']]
            targets.sort(key=lambda target:
                (-damage(attacker, target), -target['units'] * target['damage'], -target['initiative']))
            if targets and damage(attacker, targets[0]):
                targeted.add(targets[0]['id'])
                choices.append((-attacker['initiative'], attacker, targets[0]))
        choices.sort()
        for _, attacker, defender in choices:
            killed = damage(attacker, defender) // defender['hp']
            # log(f"{attacker} attacks \n {defender} \n killing {killed} units.")
            if defender['units'] <= killed:
                groups.remove(defender)
                log(f"{defender} is dead.")
            elif killed > 0:
                defender['units'] -= killed
                damage_done = True
        if not damage_done:
            log('stalemate')
            break
    return groups


start = time.perf_counter_ns()

puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = open('24.example').read()

p = compile("{units:d} units each with {hp:d} hit points {modifier:Modifier}with an attack that does {damage:d} "
            "{type} damage at initiative {initiative:d}", dict(Modifier=parse_modifier))
num_groups = 0
groups = []
for line in input_data.splitlines():
    if ':' in line:
        group_type = line[:-1]
    else:
        parsed = p.parse(line)
        if parsed:
            group = parsed.named
            group['group_type'] = group_type
            group['id'] = num_groups
            num_groups += 1
            groups.append(group)

puzzle.answer_a = unit_total(simulate(groups))
print('Part1:', puzzle.answer_a)

# debug = True

boost = 1
new_groups = simulate(groups, boost)
while Counter(group['group_type'] for group in new_groups)['Infection'] != 0:
    boost += 1
    new_groups = simulate(groups, boost)

puzzle.answer_b = unit_total(new_groups)
print('Part2:', puzzle.answer_b)

print(f"Elapsed time: {(time.perf_counter_ns() - start) / 1000000:.2f}ms")
