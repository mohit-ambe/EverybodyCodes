files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def calculate(standard, vote):
    N = len(vote)
    standard = (standard * N)[-N:]
    total = 0
    for i, (s, v) in enumerate(zip(standard, vote)):
        s, v = int(s), int(v)
        total += v * (s ** (N - i - 1))
    return total


def part1(data=dataset[0]):
    total = 0
    for line in data:
        standard, vote = line.replace("ISO-", "").split()
        total += calculate(standard, vote)
    print(total)


def part2(data=dataset[1]):
    part1(data)


def part3(data=dataset[2]):
    total = 0
    for l, line in enumerate(data):
        standard, vote = line.replace("ISO2-", "").split()
        current = calculate(standard, vote)
        for i in range(int(vote)):
            new = calculate(standard, str(i))
            if new == current:
                total -= current
                break
        total += current
    print(total)


part1()
part2()
part3()