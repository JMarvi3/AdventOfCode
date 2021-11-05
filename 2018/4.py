from collections import defaultdict, Counter
from parse import compile
from aocd.models import Puzzle

pat = compile("Guard #{guard:d} begins shift")
guards = defaultdict(Counter)
guard = start = None
for line in sorted(Puzzle(2018, 4).input_data.splitlines()):
    time_date, text = line.split('] ')
    if text[0] == 'G':
        guard = pat.parse(text)["guard"]
    elif text[0] == 'f':
        start = int(time_date[-2:])
    elif text[0] == 'w':
        end = int(time_date[-2:])
        guards[guard].update(range(start, end))

sleepiest = max(guards, key=lambda guard: sum(guards[guard].values()))
most_likely, _ = guards[sleepiest].most_common(1)[0]
print('Part1:', sleepiest * most_likely)

max_count = max_minute = max_guard = 0
for guard in guards:
    minute, count = guards[guard].most_common(1)[0]
    if count > max_count:
        max_count = guards[guard][minute]
        max_minute = minute
        max_guard = guard
print('Part2:', max_guard * max_minute)
