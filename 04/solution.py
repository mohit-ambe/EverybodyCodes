from math import ceil, floor

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    gears = list(map(int, data))
    ratio = 2025
    for i in range(len(gears) - 1):
        ratio *= gears[i] / gears[i + 1]
    print(floor(ratio))


def part2(data=dataset[1]):
    gears = list(map(int, data))
    ratio = 1
    for i in range(len(gears) - 1):
        ratio *= gears[i] / gears[i + 1]
    print(ceil(10_000_000_000_000 / ratio))


def part3(data=dataset[2]):
    gears = [list(map(int, d.split("|"))) for d in data]
    ratio = 100
    for i in range(len(gears) - 1):
        ratio *= gears[i][-1] / gears[i + 1][0]
    print(floor(ratio))


part1()
part2()
part3()
