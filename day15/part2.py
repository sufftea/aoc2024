import os
import sys
import termios
import time
import tty
from collections import deque


def read_single_keypress():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def print_map(map, dir):
    print("\n".join(["".join(row) for row in map]))
    print(f"dir: {dir}")


def parse(f):
    map = []

    for line in f:
        if line == "\n":
            break

        map.append([ch for ch in line[:-1]])

    movements = f.read().replace("\n", "")

    return map, movements


def can_move_in_dir(map, robot_x, robot_y, dx, dy, visited=None):
    if visited is None:
        visited = set()
    if (robot_x, robot_y) in visited:
        return True
    visited.add((robot_x, robot_y))

    next_x, next_y = robot_x + dx, robot_y + dy
    next = map[next_y][next_x]

    heads = set()
    if next == "[":
        heads.add((next_x, next_y))
        heads.add((next_x + 1, next_y))
    elif next == "]":
        heads.add((next_x, next_y))
        heads.add((next_x - 1, next_y))
    elif next == "#":
        return False

    can_move = True
    for head_x, head_y in heads:
        next_can_move = can_move_in_dir(map, head_x, head_y, dx, dy, visited)
        can_move = can_move and next_can_move
    return can_move


def move_in_dir(map, robot_x, robot_y, dx, dy, visited=None):
    if visited is None:
        visited = set()
    if (robot_x, robot_y) in visited:
        return
    visited.add((robot_x, robot_y))

    next_x, next_y = robot_x + dx, robot_y + dy
    next = map[next_y][next_x]

    heads = deque()
    if next == "[":
        if dx == 1:
            heads.append((next_x + 1, next_y))
            heads.append((next_x, next_y))
        elif dx == -1:
            heads.append((next_x, next_y))
        else:
            heads.append((next_x, next_y))
            heads.append((next_x + 1, next_y))
    elif next == "]":
        if dx == 1:
            heads.append((next_x, next_y))
        elif dx == -1:
            heads.append((next_x - 1, next_y))
            heads.append((next_x, next_y))
        else:
            heads.append((next_x, next_y))
            heads.append((next_x - 1, next_y))

    for head_x, head_y in heads:
        move_in_dir(map, head_x, head_y, dx, dy, visited)

    map[robot_y + dy][robot_x + dx] = map[robot_y][robot_x]
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
            if can_move_in_dir(map, robot_x, robot_y, 0, -1):
                move_in_dir(map, robot_x, robot_y, 0, -1)
        case ">":
            if can_move_in_dir(map, robot_x, robot_y, 1, 0):
                move_in_dir(map, robot_x, robot_y, 1, 0)
        case "v":
            if can_move_in_dir(map, robot_x, robot_y, 0, 1):
                move_in_dir(map, robot_x, robot_y, 0, 1)
        case "<":
            if can_move_in_dir(map, robot_x, robot_y, -1, 0):
                move_in_dir(map, robot_x, robot_y, -1, 0)


def solve(map, movements):
    for dir in movements:
        take_step(map, dir)

        os.system("cls" if os.name == "nt" else "clear")
        print_map(map, dir)
        time.sleep(0.02)
        # key = read_single_keypress()
        # print(f"you pressed: {key}")
        # if key == "q":
        #     print(f"returning")
        #     return


def calculate_score(map):
    sum = 0
    for y, row in enumerate(map):
        for x, ch in enumerate(row):
            if ch == "[":
                sum += 100 * y + x

    return sum


def transform_map(map):
    new_map = []
    for row in map:
        new_row = []
        for el in row:
            match el:
                case "#":
                    new_row += ["#", "#"]
                case ".":
                    new_row += [".", "."]
                case "@":
                    new_row += ["@", "."]
                case "O":
                    new_row += ["[", "]"]
        new_map.append(new_row)

    return new_map


with open("test1.txt") as f:
    map, movements = parse(f)

    map = transform_map(map)

    solve(map, movements)

    print_map(map, "")
    result = calculate_score(map)
    print(result)
