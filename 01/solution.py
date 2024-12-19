files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    potions = 0
    for battle in data[0]:
        if battle == "B":
            potions += 1
        elif battle == "C":
            potions += 3
    print(potions)


def part2(data=dataset[1]):
    potions = 0
    for pair in [data[0][i - 2:i] for i in range(2, len(data[0]) + 1, 2)]:
        for battle in pair:
            if battle == "B":
                potions += 1
            elif battle == "C":
                potions += 3
            elif battle == "D":
                potions += 5
        if "x" not in pair:
            potions += 2
    print(potions)


def part3(data=dataset[2]):
    potions = 0
    for trio in [data[0][i - 3:i] for i in range(3, len(data[0]) + 1, 3)]:
        for battle in trio:
            if battle == "B":
                potions += 1
            elif battle == "C":
                potions += 3
            elif battle == "D":
                potions += 5
        if "x" not in trio:
            potions += 6
        elif trio.count("x") == 1:
            potions += 2
    print(potions)


part1()
part2()
part3()
