import heapq
import sys
import termios
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


def get_neis(x, y, dir, cost):

    match dir:
        case 0:
            return [
                (x + 1, y, 0, cost + 1),
                (x, y - 1, 3, cost + 1001),
                (x, y + 1, 1, cost + 1001),
            ]
        case 1:
            return [
                (x, y + 1, 1, cost + 1),
                (x + 1, y, 0, cost + 1001),
                (x - 1, y, 2, cost + 1001),
            ]
        case 2:
            return [
                (x - 1, y, 2, cost + 1),
                (x, y - 1, 3, cost + 1001),
                (x, y + 1, 1, cost + 1001),
            ]
        case 3:
            return [
                (x, y - 1, 3, cost + 1),
                (x + 1, y, 0, cost + 1001),
                (x - 1, y, 2, cost + 1001),
            ]
        case _:
            assert False


def draw_map(map, curr_x, curr_y, curr_dir, curr_cost):

    res = []
    for y, row in enumerate(map):
        if y == curr_y:
            res.append(row[:curr_x] + "O" + row[curr_x + 1 :])
        else:
            res.append(row)
    print("\n".join(res))

    print(f"dir: {curr_dir}, cost: {curr_cost}")


def a_star(map, start_x, start_y, dir, finish_x, finish_y):
    to_visit = []

    heapq.heappush(to_visit, (0, (start_x, start_y, dir, 0)))

    visited = set()
    visited.add((start_x, start_y, dir, 0))

    finishes = []

    i = 0
    while to_visit:
        cheapest_finish = float("inf")
        if finishes:
            cheapest_finish, _ = finishes[0]

        curr_heur, curr = heapq.heappop(to_visit)
        curr_x, curr_y, curr_dir, curr_cost = curr

        if curr_cost > cheapest_finish:
            continue

        if (curr_x, curr_y, curr_dir) in visited:
            continue
        visited.add((curr_x, curr_y, curr_dir))

        if map[curr_y][curr_x] == "E":
            heapq.heappush(finishes, (curr_cost, curr))
            continue

        if i % 1000 == 0:
            # draw_map(map, curr_x, curr_y, curr_dir, curr_cost)
            print(
                f"""cost: {curr_cost}
                pos: {(curr_x, curr_y)}
                to_visit: {len(to_visit)}
                visited: {len(visited)}
                finishes: {len(finishes)}
                cheapest_finish: {cheapest_finish}

                """
            )

        i += 1

        # draw_map(map, curr_x, curr_y, curr_dir, curr_cost)
        # k = read_single_keypress()
        # if k == "q":
        #     return

        for nei in get_neis(curr_x, curr_y, curr_dir, curr_cost):
            nx, ny, nd, cost = nei
            if map[ny][nx] != "#" and nei not in visited:
                heur = abs(finish_x - nx) + abs(finish_y - ny) + cost
                heapq.heappush(to_visit, (heur, (nx, ny, nd, cost)))

    return finishes


def find_tile(map, tile):
    for y, row in enumerate(map):
        for x, curr in enumerate(row):
            if curr == tile:
                return (x, y)
    return (-1, -1)


with open("test1.txt") as f:
    map = f.read().split("\n")[:-1]

    start_x, start_y = find_tile(map, "S")
    finish_x, finish_y = find_tile(map, "E")

    result = a_star(map, start_x, start_y, 0, finish_x, finish_y)
    print(result)
