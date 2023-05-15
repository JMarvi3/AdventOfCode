from current_puzzle import current_puzzle


def calc_fuel(mass, part2=False):
    fuel = mass // 3 - 2
    total = fuel
    while part2:
        fuel = fuel // 3 - 2
        if fuel <= 0:
            break
        total += fuel
    return total


puzzle = current_puzzle()
input_data = puzzle.input_data

puzzle.answer_a = sum(map(calc_fuel, map(int, input_data.splitlines())))
puzzle.answer_b = sum(calc_fuel(mass, True) for mass in map(int, input_data.splitlines()))
