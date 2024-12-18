files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    print()


def part2(data=dataset[1]):
    print()


def part3(data=dataset[2]):
    print()


part1()
part2()
part3()
