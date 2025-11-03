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
                dx = bx - ax
                dy = by - ay

                # r = range(
                #     -int(min(ax / abs(dx), ay / abs(dy))),
                #     int(min((width - ax) / abs(dx), (height - ay) / abs(dy))) + 1,
                # )

                for n in range(-50, 50):
                    nx, ny = (ax + dx * n, ay + dy * n)
                    if nx >= 0 and nx < width and ny >= 0 and ny < height:
                        antinodes.add((nx, ny))

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
