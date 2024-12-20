files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

directions = [(-1, 0), (-0, 1), (1, -0), (0, -1)]
diagonals = [(-1, -1), (1, 1), (1, -1), (-1, 1)]


def part1(data=dataset[0], diag=False):
    layers = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#":
                layers.append((y, x))

    prev_layer = layers
    while True:
        new_layer = set()

        for y, x in prev_layer:
            safe = True
            for dy, dx in directions + (diagonals if diag else []):
                if (y + dy, x + dx) not in prev_layer:
                    safe = False
                    break

            if safe:
                new_layer.add((y, x))

        if len(new_layer) > 0:
            layers.extend(list(new_layer))
            prev_layer = new_layer
        else:
            break

    print(len(layers))


def part2(data=dataset[1]):
    part1(data)


def part3(data=dataset[2]):
    part1(data, diag=True)


part1()
part2()
part3()
