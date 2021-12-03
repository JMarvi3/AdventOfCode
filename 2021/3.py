from current_puzzle import current_puzzle
from collections import Counter

puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = open('3.example').read()

nums = input_data.splitlines()


def filter_nums(num_list, popularity):
    candidates, n, i = list(num_list), len(num_list[0]), 0
    while len(candidates) > 1:
        digit = Counter(num[i] for num in candidates).most_common()[popularity][0]
        candidates = [num for num in candidates if num[i] == digit]
        i += 1
    return candidates[0]


n = len(nums[0])
gamma = int(''.join(Counter(num[i] for num in nums).most_common()[0][0] for i in range(n)), 2)
epsilon = 2**n - 1 - gamma

puzzle.answer_a = gamma * epsilon
print('Part1:', puzzle.answer_a)

# Counter orders by first seen element if there is a tie, so make '1' come up first.
nums.sort(reverse=True)
o = int(filter_nums(nums, 0), 2)
co2 = int(filter_nums(nums, 1), 2)
puzzle.answer_b = o * co2
print('Part2:', puzzle.answer_b)
