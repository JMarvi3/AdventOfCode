from current_puzzle import current_puzzle


def draw_image(image: dict, x_range, y_range):
    for y in range(y_range[0], y_range[1] + 1):
        print(''.join('#' if image.get(x + y * 1j, 0) == 1 else '.' for x in range(x_range[0], x_range[1] + 1)))


def enhance(image: dict, algorithm: str, x_range, y_range):
    new_image = dict()
    for y in range(y_range[0], y_range[1] + 1):
        for x in range(x_range[0], x_range[1] + 1):
            index = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    index = index * 2 + image.get((x + j) + (y + i) * 1j, 0)
            # print((x, y), index, algorithm[index])
            if algorithm[index] == '#':
                new_image[x + y * 1j] = 1
    return new_image


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('20.example').read()

algorithm, field = input_data.split('\n\n')
image = dict()
for y, row in enumerate(field.splitlines()):
    for x, c in enumerate(row):
        if c == '#':
            image[x + y * 1j] = 1
x_range = [0, x]
y_range = [0, y]

print(algorithm)
x_range = x_range[0] - 10, x_range[1] + 10
y_range = y_range[0] - 10, y_range[1] + 10
image = enhance(image, algorithm, x_range, y_range)
x_range = x_range[0] + 1, x_range[1] - 1
y_range = y_range[0] + 1, y_range[1] - 1
image = enhance(image, algorithm, x_range, y_range)

print(len(image))
puzzle.answer_a = len(image)
print('Part1:', puzzle.answer_a)

image = dict()
for y, row in enumerate(field.splitlines()):
    for x, c in enumerate(row):
        if c == '#':
            image[x + y * 1j] = 1
x_range = [0, x]
y_range = [0, y]

x_range = x_range[0] - 100, x_range[1] + 100
y_range = y_range[0] - 100, y_range[1] + 100
for _ in range(25):
    image = enhance(image, algorithm, x_range, y_range)
    x_range = x_range[0] + 1, x_range[1] - 1
    y_range = y_range[0] + 1, y_range[1] - 1
    image = enhance(image, algorithm, x_range, y_range)
draw_image(image, x_range, y_range)
print(len(image))
puzzle.answer_b = len(image)
print('Part2:', puzzle.answer_b)
