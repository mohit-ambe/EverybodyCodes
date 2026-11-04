files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def solve(data):
    total = 0
    for line in data:
        softer_neighbors = dict()
        edges = line.split()
        items = set()
        for edge in edges:
            if ">" in edge:
                harder, softer = edge.split(">")
            else:
                softer, harder = edge.split("<")
            items |= {softer, harder}
            softer_neighbors[harder] = softer_neighbors.get(harder, []) + [softer]

        Q = list(softer_neighbors.keys())
        while Q:
            order = Q.pop()
            if len(order) == len(items):
                total += int(order)
                Q.clear()
                continue
            for sn in softer_neighbors.get(order[-1], []):
                if sn in order:
                    continue
                Q.append(order + sn)
    print(total)


for data in dataset:
    solve(data)