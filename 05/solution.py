files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def dance(y, people):
    clapper = people[y % len(people)].pop(0)
    destination_col = people[(y % len(people) + 1) % len(people)]
    pos = (clapper - 1) % (2 * len(destination_col))
    if pos >= len(destination_col):
        pos = 2 * len(destination_col) - pos
    destination_col.insert(pos, clapper)


def dance_routine(data):
    people = [[int(x) for x in line.split(" ")] for line in data]
    people = [list(p) for p in zip(*people)]  # transpose
    y = 0
    shouts = {0: 0}
    key = 0
    p1 = 0

    while shouts[key] != 2024:
        dance(y, people)
        key = int("".join([str(p[0]) for p in people]))
        if y == 10:
            p1 = key
        shouts[key] = shouts.get(key, 0) + 1
        y += 1
    return p1, [s[0] * y for s in shouts.items() if s[1] == 2024][0], max(shouts.keys())


def part1(data=dataset[0]):
    print(dance_routine(data)[0])


def part2(data=dataset[1]):
    print(dance_routine(data)[1])


def part3(data=dataset[2]):
    # part 2 does ~1 million iterations
    # assume the biggest number was
    # found in that processing
    print(dance_routine(data)[2])


part1()
part2()
part3()
