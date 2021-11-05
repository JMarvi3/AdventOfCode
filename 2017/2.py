from aocd.models import Puzzle

data = [list(map(int, line.split())) for line in Puzzle(2017, 2).input_data.splitlines()]
checksum = sum(max(row) - min(row) for row in data)

print('part1:', checksum)


def calc_divisible(nums):
    for i in nums:
        for j in nums:
            if i > j and i % j == 0:
                return i//j
    return None


result = sum(calc_divisible(row) for row in data)
print('part2:', result)
