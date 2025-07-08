files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

borders = 0, 1, 6, 7
# not and operation: of all set items, remove what is common
nand = lambda s1, s2:(s1 | s2) - (s1 & s2)
# sum each char's value in the runic word
power = lambda word:sum([(ord(w) - ord('A') + 1) * (i + 1) for i, w in enumerate(word)])
p1 = True


def part1(data=dataset[0]):
    global p1
    runes = sorted({d for d in "".join(data) if d.isalpha()})
    data = [[*d] for d in data]
    word = ["" for i in range(16)]
    for r in range(2, 6):
        for c in range(2, 6):
            for rune in runes:
                word[(r - 2) * 4 + (c - 2)] = "."
                if not any([(data[r][i] == rune) for i in borders]):
                    continue
                if not any([(data[i][c] == rune) for i in borders]):
                    continue
                word[(r - 2) * 4 + (c - 2)] = rune
                runes.remove(rune)
                break
    # only print on initial call
    if p1:
        print("".join(word))
    return "".join(word), runes


def part2(data=dataset[1]):
    # for each block group, unpack and rezip the lines into individual samples
    # then feed all of these to the blocks list individually
    blocks = [_ for b in range(0, len(data), 9) for _ in zip(*[l.split() for l in data[b:b + 8]])]
    print(sum([power(part1(block)[0]) for block in blocks]))


def interpolate(block):
    solved, runes = part1(block)
    block = [[*d] for d in block]
    old_block = block.copy()
    change = False

    # write in solved runes for this block
    for i in range(0, len(solved), 4):
        row = 2 + (i // 4)
        block[row] = [*block[row][:2], *solved[i:i + 4], *block[row][-2:]]

    for r in range(2, 6):
        for c in range(2, 6):
            if block[r][c] != ".":
                continue

            row_solved = {block[r][i] for i in range(2, 6)}
            row_option = {block[r][i] for i in borders}
            col_solved = {block[i][c] for i in range(2, 6)}
            col_option = {block[i][c] for i in borders}

            if '?' in row_option:
                qr, qc = r, block[r].index("?")
            else:
                q_index = [rr for rr in range(len(block)) if block[rr][c] == "?"]
                if q_index:
                    qr, qc = q_index[0], c
                else:
                    return False, False, old_block

            # find which runes are in the options, but not yet solved
            # [2:] removes . and ? from the nand result
            solution = "".join(sorted(nand(row_option, row_solved) | nand(col_option, col_solved)))[2:]

            # write in a solution if it is the ONLY candidate for the position
            if len(solution) == 1:
                block[r][c] = solution
                block[qr][qc] = solution
                change = True

    complete = all("?" not in b for b in block)
    return complete, change, block if complete else old_block


def part3(data=dataset[2]):
    data = list(data)
    select_box = lambda y, x:[l[x:x + 8] for l in data[y:y + 8]]
    completed = set()
    updated = True
    while updated:
        updated = False
        for y in range(0, len(data) - 2, 6):
            for x in range(0, len(data[0]) - 2, 6):
                if (y, x) in completed:
                    continue
                complete, change, block = interpolate(select_box(y, x))
                updated += change
                for i in range(y, y + 8):
                    data[i] = "".join([*data[i][:x], *block[i - y], *data[i][x + 8:]])
                if complete:
                    completed.add((y, x))
    print(sum([power(part1(select_box(y, x))[0]) for y, x in completed]))


part1()
p1 = False
part2()
part3()
