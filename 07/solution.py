from functools import cache

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def valid(name, rules):
    v = True
    for i in range(len(name) - 1):
        if name[i + 1] not in rules[name[i]]:
            v = False
            break
    return v


def part1(data=dataset[0]):
    names = data[0].split(",")
    rules = {d.split(" > ")[0]:d.split(" > ")[1] for d in data[2:]}

    for name in names:
        if valid(name, rules):
            print(name)
            break


def part2(data=dataset[1]):
    names = data[0].split(",")
    rules = {d.split(" > ")[0]:d.split(" > ")[1] for d in data[2:]}

    total = 0
    for j, name in enumerate(names):
        if valid(name, rules):
            total += j + 1
    print(total)


def part3(data=dataset[2]):
    names = data[0].split(",")
    rules = {d.split(" > ")[0]:d.split(" > ")[1].split(",") for d in data[2:]}

    for name in names:
        i = 0
        while i < len(names):
            n = names[i]
            if name in n and name != n:
                names.remove(n)
                i -= 1
            i += 1

    @cache
    def valid_names(idx, char):
        if idx == 11:
            return 1
        total = 1 if idx >= 7 else 0
        for adj in rules.get(char, []):
            total += valid_names(idx + 1, adj)
        return total

    print(sum([valid_names(len(name), name[-1]) for name in names if valid(name, rules)]))


part1()
part2()
part3()
