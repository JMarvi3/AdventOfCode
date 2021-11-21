from current_puzzle import current_puzzle
from itertools import combinations
import heapq
import time


def valid(floor):
    return not floor or max(floor) < 0 or all(-item in floor for item in floor if item < 0)


def get_cost(initial_state):
    q = [(0, initial_state)]
    costs = {initial_state: 0}

    while q:
        _, current_state = heapq.heappop(q)
        floor, floors = current_state
        if floor == 3 and all(len(f) == 0 for f in floors[:-1]):
            break
        for direction in (-1, 1):
            new_floor = direction + floor
            if not (0 <= new_floor < 4):
                continue
            valid_moves = list(combinations(floors[floor], 2)) + list(combinations(floors[floor], 1))
            for move in valid_moves:
                new_floors = list(floors)
                new_floors[floor] = tuple(item for item in floors[floor] if item not in move)
                new_floors[new_floor] = tuple(sorted(floors[new_floor] + move))
                if not valid(new_floors[floor]) or not valid(new_floors[new_floor]):
                    continue
                next_state = (new_floor, tuple(new_floors))
                cost = costs[current_state] + 1
                if next_state not in costs or cost < costs[next_state]:
                    costs[next_state] = cost
                    priority = cost - len(new_floors[3])*5
                    heapq.heappush(q, (priority, next_state))
    return costs[current_state]


start = time.perf_counter_ns()

puzzle = current_puzzle()

# hardcoded input     generators, microchips
polonium, thulium, promethium, ruthenium, cobalt = 1, 2, 3, 4, 5
initial = (0, (tuple(sorted((polonium, thulium, promethium, ruthenium, cobalt, -thulium, -ruthenium, -cobalt))),
               tuple(sorted((-polonium, -promethium))), (), ()))

puzzle.answer_a = get_cost(initial)
print(f"Part1: {puzzle.answer_a}, time: {(time.perf_counter_ns() - start) / 1000000:.2f}ms")
start = time.perf_counter_ns()

# hardcoded input     generators, microchips
polonium, thulium, promethium, ruthenium, cobalt, elerium, dilithium = 1, 2, 3, 4, 5, 6, 7
initial = (0, (tuple(sorted((polonium, thulium, promethium, ruthenium, cobalt, elerium, dilithium, -thulium,
                             -ruthenium, -cobalt, -elerium, -dilithium))),
               tuple(sorted((-polonium, -promethium))), (), ()))

puzzle.answer_b = get_cost(initial)
print(f"Part2: {puzzle.answer_b}, time: {(time.perf_counter_ns() - start) / 1000000:.2f}ms")

thulium, plutonium, strontium, promethium, ruthenium = 1, 2, 3, 4, 5
initial = (0, (tuple(sorted((thulium, -thulium, plutonium, strontium))), tuple(sorted((-plutonium, -strontium))),
               tuple(sorted((promethium, -promethium, ruthenium, -ruthenium))), ()))
print(get_cost(initial))

thulium, plutonium, strontium, promethium, ruthenium, elerium, dilithium = 1, 2, 3, 4, 5, 6, 7
initial = (0, (tuple(sorted((thulium, -thulium, plutonium, strontium, elerium, -elerium, dilithium, -dilithium))),
               tuple(sorted((-plutonium, -strontium))),
               tuple(sorted((promethium, -promethium, ruthenium, -ruthenium))), ()))
print(get_cost(initial))
