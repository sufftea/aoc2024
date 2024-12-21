import heapq
import re
from dataclasses import dataclass, field
from typing import Counter


def get_neis(x, y):
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


@dataclass(order=True)
class Node:
    x: int
    y: int
    cost: int
    skip_enter: tuple[int, int] | None = field(compare=False)
    skip_exit: tuple[int, int] | None = field(compare=False)


def find_path_no_cheating(field, start_x, start_y):
    to_visit = []
    heapq.heappush(to_visit, (0, Node(start_x, start_y, 0, None, None)))

    visited = {}

    while to_visit:
        _, node = heapq.heappop(to_visit)

        old_cost = visited.get((node.x, node.y), float("inf"))
        if node.cost >= old_cost:
            continue
        visited[(node.x, node.y)] = node.cost

        if field[node.y][node.x] == "E":
            return visited

        next_cost = node.cost + 1
        for nx, ny in get_neis(node.x, node.y):
            width = len(field[0])
            height = len(field)

            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue

            if field[ny][nx] == "#":
                continue

            next = Node(nx, ny, next_cost, node.skip_enter, node.skip_exit)
            if (nx, ny, next.skip_enter, next.skip_exit) not in visited:
                heur = abs(nx - width + 1) + abs(ny - height + 1)
                heapq.heappush(to_visit, (next_cost + heur, next))

    return visited


@dataclass
class Cheat:
    enter: tuple[int, int]
    exit: tuple[int, int]
    time_saved: int


def find_path_cheating(field, start_x, start_y, old_path):
    curr_x, curr_y = start_x, start_y

    saved_times = []
    visited = set()

    curr_cost = 0
    while True:
        if field[curr_y][curr_x] == "E":
            break

        visited.add((curr_x, curr_y))

        for old_pos, old_cost in old_path.items():
            if old_pos in visited:
                continue

            old_x, old_y = old_pos
            dist = abs(curr_x - old_x) + abs(curr_y - old_y)
            if dist <= 20:
                time_saved = old_cost - dist - curr_cost
                saved_times.append(time_saved)

        neis = get_neis(curr_x, curr_y)
        for nx, ny in neis:
            if (nx, ny) not in visited and field[ny][nx] != "#":
                curr_x, curr_y = nx, ny

        curr_cost += 1

    return saved_times


def find_tile(field, tile):
    for y, row in enumerate(field):
        for x, curr in enumerate(row):
            if curr == tile:
                return (x, y)
    return (-1, -1)


with open("input.txt") as f:

    field = []
    for row in f:
        field.append(list(row[:-1]))

    start = find_tile(field, "S")
    end = find_tile(field, "E")

    no_cheat_path = find_path_no_cheating(field, *start)

    cheats = find_path_cheating(field, *start, no_cheat_path)

    cheats = [cheat for cheat in cheats if cheat >= 100]
    print(len(cheats))

    # __import__("pprint").pprint(Counter(cheats))

    # cheat_costs = [cost for cost in cheat_costs if cost >= 0]
    # cheat_costs.sort()
    # cheat_costs = Counter(cheat_costs)
    # __import__("pprint").pprint(cheat_costs)
    # # sum = 0
    # for cost in cheat_costs:
    #     if cost >= 100:
    #         sum += 1
    # print(sum)
