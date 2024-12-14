import os
import re
import sys
import termios
import time
import tty


def gen_pic(robots, width, height):
    deb = [["."] * width for _ in range(height)]

    for rx, ry in robots:
        deb[ry][rx] = "#"

    pic = ["".join(row) for row in deb]
    return pic


def read_single_keypress():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def solve(robots, iters, width, height):
    # width = 11
    # height = 7

    result = []

    for px, py, vx, vy in robots:

        result.append(
            (
                (px + vx * iters) % width,
                (py + vy * iters) % height,
            ),
        )

    return result


def display_map_at_second(robots, second, width, height):
    positions = solve(robots, second, width, height)

    pic = gen_pic(positions, width, height)
    print("\n".join(pic))
    print(f"sec: {second}")


def interactive_ascii_animation(robots, entropies, width, height):
    current_frame = 0

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    try:
        while True:

            time.sleep(0.05)
            clear_screen()
            print(f"Frame {current_frame}")

            entropy, second = entropies[current_frame]
            display_map_at_second(robots, second, width, height)

            print(
                f"\n Second {second}; Entropy: {entropy} Controls: [n] Next, [p] Previous, [q] Quit"
            )

            key = read_single_keypress()

            if key == "n":  # Next frame
                current_frame = (current_frame + 1) % len(entropies)
            elif key == "p":  # Previous frame
                current_frame = (current_frame - 1) % len(entropies)
            elif key == "q":  # Quit
                clear_screen()
                print("Animation exited.")
                break
    except KeyboardInterrupt:
        clear_screen()
        print("Animation interrupted.")


with open("input.txt") as f:
    period = 10403

    robots = []
    width = 101
    height = 103

    for line in f:
        params = re.match(r"p=(\d*),(\d*) v=(\D*)(\d*),(\D*)(\d*)", line)
        assert params is not None
        (px, py, svx, vx, svy, vy) = params.groups()

        robots.append(
            (
                int(px),
                int(py),
                -int(vx) if svx == "-" else int(vx),
                -int(vy) if svy == "-" else int(vy),
            )
        )

    candidate_seconsds = []

    entropies = []
    for sec in range(period):
        positions = solve(robots, sec, width, height)

        positions = [positions[i] for i in range(0, len(positions), 6)]

        sum = 0
        for pix, piy in positions:
            for pjx, pjy in positions:
                sum += abs(pix - pjx) + abs(piy - pjy)
        entropies.append((sum, sec))
        print(f"sum: {sum}, time: {sec} / {period}")

    entropies.sort(key=lambda t: t[0])
    entropies = entropies[:500]
    entropies.reverse()

    interactive_ascii_animation(robots, entropies, width, height)
