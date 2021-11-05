from current_puzzle import current_puzzle
import re


def merge(left: dict, right: dict):
    temp = left.copy()
    for key, value in right.items():
        temp[key] += value
    return temp


def merge_timer(left: dict, key, value):
    temp = left.copy()
    temp[key] = value
    return temp


def test(boss, player, mana_spent, turn, timers, order, depth=0, part2=False):
    global min_mana, max_depth
    if turn == 0:
        min_mana = float('inf')
        max_depth = player['hp']*2
    if depth > max_depth:
        return
    if part2 and turn % 2 == 0:
        player['hp'] -= 1
        if player['hp'] <= 0:
            return
    # print(turn, timers, boss, player)
    if timers['shield'] > 0:
        timers['shield'] -= 1
        if timers['shield'] == 0:
            player['armor'] = 0
    if timers['poison'] > 0:
        timers['poison'] -= 1
        boss['hp'] -= 3
    if timers['recharge'] > 0:
        timers['recharge'] -= 1
        player['mana'] += 101
    if boss['hp'] <= 0:
        if mana_spent < min_mana:
            min_mana = mana_spent
            max_depth = depth
        return
    if turn % 2 == 1:  # BOSS
        damage = max(1, boss['damage'] - player['armor'])
        player['hp'] -= damage
        if player['hp'] <= 0:
            return
        test(boss, player, mana_spent, turn + 1, timers, order, depth + 1, part2)
    else:  # PLAYER
        # Try each spell
        # Magic Missile
        if player['mana'] >= 53:
            # print(turn, 'mm')
            test(merge(boss, {'hp': -4}), merge(player, {'mana': -53}),
                 mana_spent + 53, turn + 1, timers.copy(), order + ['M'], depth + 1, part2)
        # Drain
        if player['mana'] >= 73:
            # print(turn, 'drain')
            test(merge(boss, {'hp': -2}), merge(player, {'hp': +2, 'mana': -73}),
                 mana_spent + 73, turn + 1, timers.copy(), order + ['D'], depth + 1, part2)
        # Shield
        if player['mana'] >= 113 and timers['shield'] == 0:
            # print(turn, 'shield')
            test(boss.copy(), merge(player, {'armor': +7, 'mana': -113}),
                 mana_spent + 113, turn + 1, merge_timer(timers, 'shield', 6), order + ['S'], depth + 1, part2)
        # Poison
        if player['mana'] >= 173 and timers['poison'] == 0:
            # print(turn, 'poison')
            test(boss.copy(), merge(player, {'mana': -173}),
                 mana_spent + 173, turn + 1, merge_timer(timers, 'poison', 6), order + ['P'], depth + 1, part2)
        # Recharge
        if player['mana'] >= 229 and timers['recharge'] == 0:
            # print(turn, 'recharge')
            test(boss.copy(), merge(player, {'mana': -229}),
                 mana_spent + 229, turn + 1, merge_timer(timers, 'recharge', 5), order + ['R'], depth + 1, part2)


puzzle = current_puzzle()
input_data = puzzle.input_data

bh, bd = map(int, re.findall(r'\d+', input_data))
boss_init = {'hp': bh, 'damage': bd}
player_init = {'hp': 50, 'mana': 500, 'armor': 0}
timers = {'shield': 0, 'poison': 0, 'recharge': 0}

min_mana = float('inf')
# test({'hp': 13, 'damage': 8}, {'hp': 10, 'mana': 250, 'armor': 0}, 0, 0, timers.copy(), [])  # 226
# print(min_mana)
# test({'hp': 14, 'damage': 8}, {'hp': 10, 'mana': 250, 'armor': 0}, 0, 0, timers.copy(), [])  # 641
# print(min_mana)
# test({'hp': 58, 'damage': 9}, {'hp': 50, 'mana': 500, 'armor': 0}, 0, 0, timers.copy(), [])  # 1269
# print(min_mana)
test(boss_init.copy(), player_init.copy(), 0, 0, timers.copy(), [])

puzzle.answer_a = min_mana
print('Part1:', puzzle.answer_a)


min_mana = float('inf')
# test({'hp': 58, 'damage': 9}, {'hp': 50, 'mana': 500, 'armor': 0}, 0, 0, timers.copy(), [], part2=True)  # 1309
# print(min_mana)
test(boss_init.copy(), player_init.copy(), 0, 0, timers.copy(), [], part2=True)

puzzle.answer_b = min_mana
print('Part2:', puzzle.answer_b)
