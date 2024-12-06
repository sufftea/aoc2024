def find_start(field):
    for y, row in enumerate(field):
        for x, char in enumerate(row):
            if char == "^":
                return (x, y)
    return (-1, -1)


class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


def has_loop(field, curr_x, curr_y, curr_dir):
    visited = set()
    while True:
        if (curr_x, curr_y, curr_dir) in visited:
            return True

        next_x, next_y = (curr_x, curr_y)
        visited.add((curr_x, curr_y, curr_dir))

        match curr_dir:
            case Direction.UP:
                next_y -= 1
            case Direction.RIGHT:
                next_x += 1
            case Direction.DOWN:
                next_y += 1
            case Direction.LEFT:
                next_x -= 1

        if not (
            next_y < len(field)
            and next_y >= 0
            and next_x < len(field[next_y])
            and next_x >= 0
        ):
            return False

        if field[next_y][next_x] == "#":
            match curr_dir:
                case Direction.UP:
                    curr_dir = Direction.RIGHT
                case Direction.RIGHT:
                    curr_dir = Direction.DOWN
                case Direction.DOWN:
                    curr_dir = Direction.LEFT
                case Direction.LEFT:
                    curr_dir = Direction.UP
        else:
            curr_x, curr_y = next_x, next_y


def add_obstacle(field, obstacle_x, obstacle_y):
    result = []
    for y, row in enumerate(field):
        if y == obstacle_y:
            result.append(row[:obstacle_x] + "#" + row[obstacle_x + 1 :])
        else:
            result.append(row)
    return result


def run(field, curr_x, curr_y):
    start_x, start_y = curr_x, curr_y
    curr_dir = Direction.UP

    visited = set()

    possible_loops = 0
    while True:
        next_x, next_y = (curr_x, curr_y)
        visited.add((curr_x, curr_y))

        match curr_dir:
            case Direction.UP:
                next_y -= 1
            case Direction.RIGHT:
                next_x += 1
            case Direction.DOWN:
                next_y += 1
            case Direction.LEFT:
                next_x -= 1

        if not (
            next_y < len(field)
            and next_y >= 0
            and next_x < len(field[next_y])
            and next_x >= 0
        ):
            return possible_loops

        if field[next_y][next_x] == "#":
            match curr_dir:
                case Direction.UP:
                    curr_dir = Direction.RIGHT
                case Direction.RIGHT:
                    curr_dir = Direction.DOWN
                case Direction.DOWN:
                    curr_dir = Direction.LEFT
                case Direction.LEFT:
                    curr_dir = Direction.UP
        else:
            if (next_x, next_y) not in visited:
                possible_field = add_obstacle(field, next_x, next_y)
                if has_loop(possible_field, curr_x, curr_y, curr_dir):
                    possible_loops += 1

            curr_x, curr_y = next_x, next_y


with open("input.txt") as f:
    field = f.read().split("\n")
    (curr_x, curr_y) = find_start(field)
    result = run(field, curr_x, curr_y)
    print(result)
