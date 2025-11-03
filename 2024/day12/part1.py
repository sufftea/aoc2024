from collections import deque


def get_neis(x, y, field):
    curr = field[y][x]

    offsets = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    for ox, oy in offsets:
        if field[y + oy][x + ox]:
            pass


def fill_region(x, y, field, global_visited):

    local_visited = set()

    to_visit = deque()
    to_visit.append((x, y))
    local_visited.add((x, y))
    visited_fences = set()

    while len(to_visit) > 0:
        x, y = to_visit.popleft()
        curr = field[y][x]

        offsets = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        for ox, oy in offsets:
            nei_x = x + ox
            nei_y = y + oy

            nei = field[nei_y][nei_x]
            if curr == nei and (nei_x, nei_y) not in local_visited:
                local_visited.add((nei_x, nei_y))
                to_visit.append((nei_x, nei_y))
            elif curr != nei:
                visited_fences.add((nei_x, nei_y, ox, oy))

    visited_fences_twice = set()
    perimeter = 0
    for x, y, ox, oy in visited_fences:
        if ox == 0:
            a = (x + 1, y, ox, oy)
            b = (x - 1, y, ox, oy)

            if b not in visited_fences:
                perimeter += 1

        elif oy == 0:
            a = (x, y + 1, ox, oy)
            b = (x, y - 1, ox, oy)
            if b not in visited_fences:
                perimeter += 1

    global_visited.update(local_visited)
    return (len(local_visited), perimeter)


def run(field):
    visited_plots = set()

    regions = []
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "+":
                continue
            if (x, y) not in visited_plots:
                value = fill_region(x, y, field, visited_plots)
                regions.append((field[y][x], value, value[0] * value[1]))

    return regions


with open("input.txt") as f:
    field = f.read().split("\n")[:-1]

    field = [("+" + plots + "+") for plots in field]
    field = ["+" * len(field[0])] + field
    field = field + ["+" * len(field[0])]

    __import__("pprint").pprint(field)
    result = run(field)

    __import__("pprint").pprint(result)
    sum = 0
    for _, _, mul in result:
        sum += mul
    print(sum)
