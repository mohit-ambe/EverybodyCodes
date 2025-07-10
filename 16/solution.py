from functools import cache
from math import lcm

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line for line in file.readlines()) for file in files]
[f.close() for f in files]


def parse(data):
    t = list(map(int, data[0].split(",")))

    ww = [[] for _ in range(len(t))]
    for line in data[2:]:
        for i in range(0, len(line), 4):
            if cat := line[i:i + 3].strip():
                ww[i // 4].append(cat)

    return t, ww


def score(roll):
    count = dict()
    for face in roll.split():
        e1, e2 = face[0], face[-1]
        count[e1] = count.get(e1, 0) + 1
        count[e2] = count.get(e2, 0) + 1

    return sum([1 + count[c] - 3 for c in count if count[c] >= 3])


def part1(data=dataset[0]):
    turns, wheels = parse(data)
    print(" ".join([wheel[(100 * turns[t]) % len(wheel)] for t, wheel in enumerate(wheels)]))


def part2(data=dataset[1]):
    PULLS = 202420242024
    turns, wheels = parse(data)
    cycle_length = lcm(*map(len, wheels))
    num_cycles = (PULLS // cycle_length)
    total_score = 0

    i = 1
    while i < PULLS:
        roll = " ".join([wheel[(i * turns[t]) % len(wheel)] for t, wheel in enumerate(wheels)])
        total_score += score(roll) * num_cycles
        if i == cycle_length:
            i = num_cycles * cycle_length
            num_cycles = 1
        else:
            i += 1

    print(total_score)


def part3(data=dataset[2]):
    turns, wheels = parse(data)
    right_pulls = 256

    @cache
    def two_lever_machine(left, right):
        roll = " ".join([wheel[(right * turns[t] + left) % len(wheel)] for t, wheel in enumerate(wheels)])
        s = score(roll) if right else 0
        if right == right_pulls:
            return s, s
        scores = [two_lever_machine(left + i, right + 1) for i in [-1, 0, 1]]
        return s + max([mx for mx, mn in scores]), s + min([mn for mx, mn in scores])

    print(*two_lever_machine(0, 0))


part1()
part2()
part3()
