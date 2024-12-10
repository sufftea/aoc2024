def run(field):
    width = len(field[0])
    height = len(field)

    antena_types = {}

    for y, row in enumerate(field):
        for x, name in enumerate(row):
            if name != ".":
                if name not in antena_types:
                    antena_types[name] = [(x, y)]
                else:
                    antena_types[name].append((x, y))

    # __import__("pprint").pprint(antena_types)
    antinodes = set()
    for antenaes in antena_types.values():
        for i, antena_a in enumerate(antenaes):
            for antena_b in antenaes[:i]:
                ax, ay = antena_a
                bx, by = antena_b

                x1 = 2 * ax - bx
                y1 = 2 * ay - by
                x2 = 2 * bx - ax
                y2 = 2 * by - ay

                if x1 >= 0 and x1 < width and y1 >= 0 and y1 < height:
                    antinodes.add((x1, y1))
                if x2 >= 0 and x2 < width and y2 >= 0 and y2 < height:
                    antinodes.add((x2, y2))

    # print(antinodes)
    return len(antinodes)


with open("input.txt") as f:
    field = f.read().split("\n")[:-1]

    result = run(field)
    print(result)
    # for y, row in enumerate(field):
    #     for x, point in enumerate(row):
    #         if (x, y) in result:
    #             print("#", end="")
    #         else:
    #             print(point, end="")
    #     print()
