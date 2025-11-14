files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    names = data[0].split(",")
    dirs = [[d[0], d[1:]] for d in data[2].split(",")]
    i = 0
    for d, x in dirs:
        i += (1 if d == "R" else -1) * int(x)
        i = min(max(i, 0), len(names) - 1)

    print(names[i])


def part2(data=dataset[1]):
    names = data[0].split(",")
    dirs = [[d[0], d[1:]] for d in data[2].split(",")]
    i = 0
    for d, x in dirs:
        i += (1 if d == "R" else -1) * int(x)

    print(names[i % len(names)])


def part3(data=dataset[2]):
    names = data[0].split(",")
    dirs = [[d[0], d[1:]] for d in data[2].split(",")]
    for d, x in dirs:
        i = (1 if d == "R" else -1) * int(x) % len(names)
        names[0], names[i] = names[i], names[0]

    print(names[0])


part1()
part2()
part3()
