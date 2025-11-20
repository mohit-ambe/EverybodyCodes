files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    i = data[0].find("A")
    total = 0
    while 0 <= i < len(data[0]):
        total += data[0][i + 1:].count("a")
        i = data[0].find("A", i + 1)
    print(total)


def part2(data=dataset[1]):
    total = 0
    for mentor in "ABC":
        i = data[0].find(mentor)
        while 0 <= i < len(data[0]):
            total += data[0][i + 1:].count(mentor.lower())
            i = data[0].find(mentor, i + 1)
    print(total)


def find_by_distance(data, reps=1000, dist=1000):
    total = 0
    data = data * reps

    for i in [x for x in range(len(data)) if data[x].islower()]:
        total += data[max(0, i - dist):min(len(data), i + dist) + 1].count(data[i].upper())

    return total


def part3(data=dataset[2]):
    # when len(data) > 1000,
    # find_by_distance increases linearly.
    # find the relationship using
    # the first two repetitions:

    # slope = (f(2) - f(1)) / (2 - 1)
    # intercept = f(1)
    # f(1000) = intercept + slope * 999

    b = find_by_distance(data[0], 1, 1000)
    m = find_by_distance(data[0], 2, 1000) - b
    print(b + 999 * m)


part1()
part2()
part3()
