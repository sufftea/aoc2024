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


def get_neis_reverse(x, y, dir, cost):

    match dir:
        case 0:
            return [
                (x - 1, y, 0, cost - 1),
                (x - 1, y, 3, cost - 1001),
                (x - 1, y, 1, cost - 1001),
            ]
        case 1:
            return [
                (x, y - 1, 1, cost - 1),
                (x, y - 1, 0, cost - 1001),
                (x, y - 1, 2, cost - 1001),
            ]
        case 2:
            return [
                (x + 1, y, 2, cost - 1),
                (x + 1, y, 3, cost - 1001),
                (x + 1, y, 1, cost - 1001),
            ]
        case 3:
            return [
                (x, y + 1, 3, cost - 1),
                (x, y + 1, 0, cost - 1001),
                (x, y + 1, 2, cost - 1001),
            ]
        case _:
            assert False


def draw_map(map, special_tiles):

    mutable_map = [list(row) for row in map]

    for x, y, char in special_tiles:
        mutable_map[y][x] = char

    print("\n".join("".join(row) for row in mutable_map))


def a_star(map, start_x, start_y, dir, finish_x, finish_y):
    to_visit = []

    heapq.heappush(to_visit, (0, (start_x, start_y, dir, 0)))

    visited = {}
    # visited[(start_x, start_y, dir)] = 0

    finishes = []

    while to_visit:
        cheapest_finish = float("inf")
        if finishes:
            cheapest_finish, _ = finishes[0]

        _, curr = heapq.heappop(to_visit)
        curr_x, curr_y, curr_dir, curr_cost = curr

        if curr_cost > cheapest_finish:
            continue

        old_cost = visited.get((curr_x, curr_y, curr_dir), float("inf"))
        if curr_cost > old_cost:
            continue
        visited[(curr_x, curr_y, curr_dir)] = curr_cost

        if map[curr_y][curr_x] == "E":
            heapq.heappush(finishes, (curr_cost, curr_dir))
            continue

        # print("===")
        # print(f"last visited: {list( visited.keys() )[-1]}")
        # print(f"position: {(curr_x, curr_y, curr_dir)}")
        # draw_map(map, [(curr_x, curr_y, "0")])
        # k = read_single_keypress()
        # if k == "q":
        #     return

        for nei in get_neis(curr_x, curr_y, curr_dir, curr_cost):
            nx, ny, nd, cost = nei
            # old_cost = visited.get((nx, ny, nd), float("inf"))
            if map[ny][nx] != "#":
                heur = abs(finish_x - nx) + abs(finish_y - ny) + cost
                heapq.heappush(to_visit, (heur, (nx, ny, nd, cost)))

    return finishes, visited


def trace_back(map, curr_x, curr_y, curr_dir, curr_cost, visited_costs, best_paths):
    best_paths.append((curr_x, curr_y))

    neis = get_neis_reverse(curr_x, curr_y, curr_dir, curr_cost)
    for nei in neis:
        nei_x, nei_y, nei_dir, nei_cost = nei
        position = (nei_x, nei_y, nei_dir)
        if position in visited_costs and visited_costs[position] == nei_cost:
            trace_back(map, nei_x, nei_y, nei_dir, nei_cost, visited_costs, best_paths)


def find_tile(map, tile):
    for y, row in enumerate(map):
        for x, curr in enumerate(row):
            if curr == tile:
                return (x, y)
    return (-1, -1)


with open("input.txt") as f:
    field = f.read().split("\n")[:-1]

    start_x, start_y = find_tile(field, "S")
    finish_x, finish_y = find_tile(field, "E")

    finishes, visited_costs = a_star(field, start_x, start_y, 0, finish_x, finish_y)
    print(finishes)

    # visited_costs = {(x, y): cost for (x, y, _), cost in visited_costs.items()}

    best_paths = []
    for finish_cost, finish_dir in finishes:
        trace_back(
            field,
            finish_x,
            finish_y,
            finish_dir,
            finish_cost,
            visited_costs,
            best_paths,
        )

    print(best_paths)

    # draw_map(field, map(lambda pos: (pos[0], pos[1], "O"), best_paths))

    print(len(set(best_paths)))
    # finish_cost, _ = finishes[0]
    # trace_back(map, finish_x, finish_y, )
