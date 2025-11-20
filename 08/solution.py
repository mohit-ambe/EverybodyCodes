files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    pins = list(map(int, data[0].split(",")))
    semi = max(pins) // 2
    intersects = 0
    for i in range(len(pins) - 1):
        if abs(pins[i + 1] - pins[i]) == semi:
            intersects += 1
    print(intersects)


def part2(data=dataset[1]):
    pins = list(map(int, data[0].split(",")))
    strings = list(zip(pins, pins[1:]))
    knots = 0

    for i, string in enumerate(strings):
        a, b = min(string), max(string)
        for s in strings[:i]:
            x, y = min(s), max(s)
            if a == x or b == y:
                continue
            if (x < a < y) != (x < b < y):
                knots += 1

    print(knots)


def part3(data=dataset[2]):
    pins = list(map(int, data[0].split(",")))
    strings = list(zip(pins, pins[1:]))
    knots = 0

    for a in range(1, max(pins) + 1):
        for b in range(a + 1, max(pins) + 1):
            k = 1 if ((a, b) in strings or (b, a) in strings) else 0
            for s in strings:
                x, y = min(s), max(s)
                if a == x or b == y:
                    continue
                if (x < a < y) != (x < b < y):
                    k += 1
            knots = max(knots, k)

    print(knots)


part1()
part2()
part3()
