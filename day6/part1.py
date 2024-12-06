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


def foo(curr_x, curr_y):
    curr_dir = Direction.UP
    visited = set()
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
            return len(visited)

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


with open("input.txt") as f:
    field = f.read().split("\n")

    (curr_x, curr_y) = find_start(field)
    result = foo(curr_x, curr_y)

    print(result)
