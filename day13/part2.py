import math
import re


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def solve_machine(ax, bx, px):

    gcd, a_inverse, _ = gcdExtended(ax, bx)
    if px % gcd != 0:
        return None

    ax = ax // gcd
    bx = bx // gcd
    px = px // gcd

    gcd, a_inverse, _ = gcdExtended(ax, bx)

    an = px * a_inverse
    an = an % bx

    return (an, bx)


# p - a * n == 0 (mod b)
# p == a * n (mod b)
# a * n == p (mod b)
# d == gcd(a, b),
# p / d == a * n / d ( mod (b / d) ), only if p is divisible by d
# n = p * a_inverse ( mod (b / d) )
#
# n + b/d * k -- all the solutions
#
#
# now, do the same for both axises
#
# we get:
# a1 + b1 * kx = n
# a2 + b2 * ky = n
#
# i need them both equal
#
# a1 + b1 * kx = a2 + b2 * ky
# a1 - a2 = b2 * ky - b1 * kx
#
#
#


def try_all(equation_x, a, b, prize):
    (ea, eb) = equation_x

    px, py = prize
    ax, ay = a
    bx, by = b

    # (ea + k * eb) * ax = px
    # ea * ax + k * eb * ax = px
    # k * eb * ax = px - ea * ax

    min_k = 0
    max_k = (px - ea * ax) / (eb * ax)
    max_k = math.ceil(max_k) + 1
    k = min_k
    visited = set()
    # k = 0
    while True:
        an = ea + k * eb
        bn = (px - ax * an) / bx
        bn = int(bn)

        endx = an * ax + bn * bx
        endy = an * ay + bn * by

        # print(f"checking k={k}; (an, bn)=({an}, {bn}); diffy=({endy - py})")

        if k in visited:
            return None
        visited.add(k)

        if endx == px and endy == py:
            return (an, bn)
        if endy > py:
            nan = an + eb
            nbn = (px - ax * nan) / bx
            nendy = nan * ay + nbn * by
            if nendy < endy:
                min_k = k
                k = k + math.ceil((max_k - k) / 2)
            else:
                max_k = k
                k = k - math.ceil((k - min_k) / 2)
        elif endy < py:
            nan = an + eb
            nbn = (px - ax * nan) / bx
            nendy = nan * ay + nbn * by
            if nendy > endy:
                min_k = k
                k = k + math.ceil((max_k - k) / 2)
            else:
                max_k = k
                k = k - math.ceil((k - min_k) / 2)
        elif endx == px and endy == py:
            return (an, bn)


with open("input.txt") as f:

    sum = 0
    while f:
        a = re.match(r"^Button A: X\+(\d*), Y\+(\d*)$", f.readline())
        assert a
        a = list(map(int, a.groups()))

        b = re.match(r"^Button B: X\+(\d*), Y\+(\d*)$", f.readline())
        assert b
        b = list(map(int, b.groups()))

        prize = re.match(r"Prize: X=(\d*), Y=(\d*)", f.readline())
        assert prize
        prize = list(map(int, prize.groups()))

        prize[0] += 10000000000000
        prize[1] += 10000000000000

        print(a, b, prize)

        px, py = prize

        ax, ay = a
        bx, by = b

        # find the preferred button.

        ax_value = ax / 3
        bx_value = bx

        ay_value = ay / 3
        by_value = by

        a_value = ax_value * ay_value
        b_value = bx_value * by_value

        prefer_a = a_value > b_value
        prefer_a = False
        #
        # ...

        solution_x = solve_machine(ax, bx, px)
        solution_y = solve_machine(ay, by, py)
        # print(solution_x, solution_y)

        if solution_x is not None and solution_y is not None:
            solution = None
            if prefer_a:
                solution = try_all(solution_y, b, a, prize)
            else:
                solution = try_all(solution_x, a, b, prize)

            if solution is not None:
                an, bn = solution

                value = an * 3 + bn
                print(f"solution: {solution}, value: {value}")
                sum += value
            else:
                print("no solution")
        else:
            print("no solution")

        l = f.readline()
        if not l:
            break
    print("=======================================")
    print(sum)
