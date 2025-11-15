files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    crates = sorted([int(x) for x in data[0].split(",")], reverse=True)
    prev = 1e10
    sum = 0
    i = 0
    while i < len(crates):
        if crates[i] < prev:
            sum += crates[i]
            prev = crates[i]
        i += 1
    print(sum)


def part2(data=dataset[1]):
    crates = sorted([int(x) for x in data[0].split(",")])
    prev = 0
    sum = 0
    count = 0
    i = 0
    while i < len(crates) and count < 20:
        if crates[i] > prev:
            sum += crates[i]
            prev = crates[i]
            count += 1
        i += 1
    print(sum)


def part3(data=dataset[2]):
    # crate sequences can contain a size n only once
    # so, the minimum sets is the maximum frequency of a size n
    crates = data[0].split(",")
    print(max([crates.count(c) for c in set(crates)]))


part1()
part2()
part3()
