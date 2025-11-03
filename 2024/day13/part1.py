import re


def solve_machine(a, b, prize):
    px, py = prize
    ax, ay = a
    bx, by = b
    max_bees = min(px // bx, py // by) + 1
    for nof_bees in reversed(range(101)):
        endx = px - bx * nof_bees
        endy = py - by * nof_bees
        if endx % ax == 0 and endy % ay == 0:
            stepsax = endx // ax
            stepsay = endy // ay
            stepb = nof_bees

            if (
                stepsax == stepsay
                and stepsax >= 0
                and stepsay <= 100
                and stepb >= 0
                and stepb <= 100
            ):
                return (stepsax, stepb)
    return None


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

        print(a, b, prize)

        solution = solve_machine(a, b, prize)
        if solution:
            an, bn = solution
            # sum += an * 3 + bn
            value = an * 3 + bn
            print(f"solution: {solution}, value: {value}")
            sum += value
        else:
            print("no solution")

        # print(solution)

        l = f.readline()
        if not l:
            break
    print(sum)
