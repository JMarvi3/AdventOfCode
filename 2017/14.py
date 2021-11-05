from aocd.models import Puzzle
from functools import reduce
from operator import xor
from collections import deque


def knot_hash(key):
    lengths = list(map(ord, key)) + [17, 31, 73, 47, 23]
    pos = skip = 0
    n = 256
    nums = list(range(n))
    for _ in range(64):
        for length in lengths:
            left, right = pos, pos + length - 1
            while left < right:
                nums[left % n], nums[right % n] = nums[right % n], nums[left % n]
                left += 1
                right -= 1
            pos = (pos + length + skip) % n
            skip += 1
    return ''.join(f"{reduce(xor, nums[i:i + 16]):02x}" for i in range(0, 256, 16))


def count_bits(h):
    num = int(h, 16)
    bits = 0
    while num > 0:
        bits += num & 1
        num >>= 1
    return bits


def dfs(start, visited, hashes):
    q = deque([start])
    while q:
        node = q.pop()
        if node not in visited:
            visited.add(node)
            for move in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                x, y = node[0] + move[0], node[1] + move[1]
                if 0 <= x <= 127 and 0 <= y <= 127 and hashes[x][y] == '1':
                    q.appendleft((x, y))


master_key = Puzzle(2017, 14).input_data.strip() + "-"
#master_key = "flqrgnkx-"
hashes = [int(knot_hash(master_key + str(row)), 16) for row in range(128)]
bin_hashes = [f"{hash:0128b}" for hash in hashes]

print('Part1:', sum(hash.count("1") for hash in bin_hashes))

visited = set()
regions = 0
for x in range(128):
    for y in range(128):
        if bin_hashes[x][y] == '1' and (x, y) not in visited:
            regions += 1
            dfs((x, y), visited, bin_hashes)

print('Part2:', regions)
