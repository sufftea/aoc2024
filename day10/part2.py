from collections import deque


def get_neighbors(field, pos_x, pos_y):
    neighbors = []

    curr_value = field[pos_y][pos_x]

    candidates = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    for candidate in candidates:
        x = pos_x + candidate[0]
        y = pos_y + candidate[1]

        if (
            x >= 0
            and x < len(field[0])
            and y >= 0
            and y < len(field)
            and field[y][x] == curr_value + 1
        ):
            neighbors.append((x, y))

    return neighbors


def calculate_score(field, head_x, head_y):
    finishes = []

    neis = deque()
    neis.append((head_x, head_y))

    # visited = set()

    while len(neis) > 0:
        curr = neis.popleft()

        curr_value = field[curr[1]][curr[0]]
        if curr_value == 9:
            finishes.append(curr)
            continue

        new_neis = get_neighbors(field, curr[0], curr[1])
        neis.extend(new_neis)

    return len(finishes)


def find_heads(field):
    heads = []
    for y, row in enumerate(field):
        for x, value in enumerate(row):
            if value == 0:
                heads.append((x, y))
    return heads


with open("input.txt") as f:
    field = f.read().split("\n")[:-1]
    field = [list(map(int, row)) for row in field]
    # print(field)

    heads = find_heads(field)
    sum = 0
    for head in heads:
        score = calculate_score(field, head[0], head[1])
        sum += score
    print(sum)
