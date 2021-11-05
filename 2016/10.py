from aocd.models import Puzzle
from collections import defaultdict
import re

value_pat = re.compile(r'value (\d+) goes to bot (\d+)')
rule_pat = re.compile(r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)')

bots = defaultdict(list)
outputs = dict()
rules = dict()
answer = None
bots_to_process = []
for line in Puzzle(2016, 10).input_data.splitlines():
    if line[0] == 'v':
        value, bot = [int(n) for n in value_pat.match(line).groups()]
        bots[bot].append(value)
        if len(bots[bot]) == 2:
            bots_to_process.append(bot)
    else:
        bot, *rule = rule_pat.match(line).groups()
        bot = int(bot)
        rule[1] = int(rule[1])
        rule[3] = int(rule[3])
        rules[bot] = rule

while bots_to_process:
    bot = bots_to_process.pop()
    if 17 in bots[bot] and 61 in bots[bot]:
        answer = bot
    values = [int(n) for n in sorted(bots[bot])]
    rule = rules[bot]
    nums = [int(rule[1]), int(rule[3])]
    if rule[0] == 'output':
        outputs[nums[0]] = values[0]
    else:
        bots[nums[0]].append(values[0])
        if len(bots[nums[0]]) == 2:
            bots_to_process.append(nums[0])
    if rule[2] == 'output':
        outputs[nums[1]] = values[1]
    else:
        bots[nums[1]].append(values[1])
        if len(bots[nums[1]]) == 2:
            bots_to_process.append(nums[1])
    bots[bot] = []

print('part1:', answer)
print('part2:', outputs[0] * outputs[1] * outputs[2])
