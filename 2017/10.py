from aocd.models import Puzzle
from functools import reduce
from operator import xor


def reverse(nums, left, right, n):
    while left < right:
        nums[left % n], nums[right % n] = nums[right % n], nums[left % n]
        left += 1
        right -= 1


def do_cycle(nums, lengths, pos, skip, n):
    for length in lengths:
        reverse(nums, pos, pos + length - 1, n)
        pos = (pos + length + skip) % n
        skip += 1
    return pos, skip


input_data = Puzzle(2017, 10).input_data
n = 256
lengths = list(map(int, input_data.split(",")))
nums = list(range(n))
do_cycle(nums, lengths, 0, 0, n)

print('Part1:', nums[0]*nums[1])

lengths = list(map(ord, input_data)) + [17, 31, 73, 47, 23]
nums = list(range(n))
pos = skip = 0
for _ in range(64):
    pos, skip = do_cycle(nums, lengths, pos, skip, n)

dense_hash = ''.join(f"{reduce(xor, nums[i:i+16]):02x}" for i in range(0, 256, 16))
print('Part2:', dense_hash)
