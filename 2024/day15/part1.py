def print_map(map):
    print("\n".join(["".join(row) for row in map]))


def parse(f):
    map = []

    for line in f:
        if line == "\n":
            break

        map.append([ch for ch in line[:-1]])

    movements = f.read().replace("\n", "")

    return map, movements


def move_in_dir(map, robot_x, robot_y, dx, dy):
    head_x, head_y = robot_x, robot_y

    while map[head_y + dy][head_x + dx] == "O":
        head_x += dx
        head_y += dy

    if map[head_y + dy][head_x + dx] != "#":
        map[head_y + dy][head_x + dx] = "O"
        map[robot_y + dy][robot_x + dx] = "@"
        map[robot_y][robot_x] = " "


def take_step(map, dir):
    robot_x, robot_y = 0, 0

    for y, row in enumerate(map):
        if "@" in row:
            x = row.index("@")
            if x >= 0:
                robot_x = x
                robot_y = y
                break

    match dir:
        case "^":
            move_in_dir(map, robot_x, robot_y, 0, -1)
        case ">":
            move_in_dir(map, robot_x, robot_y, 1, 0)
        case "v":
            move_in_dir(map, robot_x, robot_y, 0, 1)
        case "<":
            move_in_dir(map, robot_x, robot_y, -1, 0)


def solve(map, movements):
    for move in movements:
        take_step(map, move)


def calculate_score(map):
    sum = 0

    for y, row in enumerate(map):
        for x, ch in enumerate(row):
            if ch == "O":
                sum += 100 * y + x

    return sum


with open("input.txt") as f:
    map, movements = parse(f)

    solve(map, movements)

    result = calculate_score(map)
    print(result)
