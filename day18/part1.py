import heapq
import re


def draw_map(field, special_tiles):
    mutable_field = [list(row) for row in field]

    for x, y, char in special_tiles:
        mutable_field[y][x] = char

    print("\n".join("".join(row) for row in mutable_field))


def get_neis(x, y):
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def find_path(obstacles, width, height, second):
    to_visit = []
    heapq.heappush(to_visit, (0, (0, 0, 0)))

    visited = {}

    while to_visit:
        _, (cx, cy, curr_cost) = heapq.heappop(to_visit)

        old_cost = visited.get((cx, cy), float("inf"))
        if curr_cost >= old_cost:
            continue
        visited[(cx, cy)] = curr_cost

        if obstacles.get((cx, cy), float("inf")) < second:
            continue
        if (cx, cy) == (width - 1, height - 1):
            return curr_cost

        # print(
        #     f"""
        #     visited: {len(visited)}
        #     to_visit: {len(to_visit)}
        #
        #     curr_cost: {curr_cost}
        # """
        # )

        # draw_map(field, [(cx, cy, "O")])
        # print()

        next_cost = curr_cost + 1
        for nei in get_neis(cx, cy):
            nx, ny = nei
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue

            heur = abs(nx - width + 1) + abs(ny - height + 1)
            if nei not in visited:
                heapq.heappush(to_visit, (next_cost + heur, (nx, ny, next_cost)))

    return None


with open("input.txt") as f:
    WIDTH, HEIGHT = 71, 71
    # WIDTH, HEIGHT = 7, 7

    obstacles = {}
    for i, l in enumerate(list(f)):
        coords = re.findall(r"\d+", l)
        x, y = map(int, coords)

        if (x, y) not in obstacles:
            obstacles[(x, y)] = i

    # field = [["."] * (WIDTH) for _ in range(HEIGHT)]
    # for obs, i in obstacles.items():
    #     if i > 12:
    #         continue
    #     x, y = obs
    #     field[y][x] = "#"
    #
    # draw_map(field, [])

    for i in range(0, len(obstacles)):

        cost = find_path(obstacles, WIDTH, HEIGHT, i)
        print(f"i: {i}/{len(obstacles)} \t; cost: {cost},")
        if cost is None:
            for coords, j in obstacles.items():
                if j == i - 1:
                    print(f"coords: {coords}")
                    break

            break
