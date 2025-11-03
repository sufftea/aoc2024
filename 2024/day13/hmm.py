import re


def solve_machine(a, b, prize):
    px, _ = prize
    ax, _ = a
    bx, _ = b
    max_bees = px // bx + 1
    for nof_bees in reversed(range(max_bees)):
        endx = px - bx * nof_bees
        if endx % ax == 0:
            stepsax = endx // ax
            stepb = nof_bees

            if stepsax >= 0 and stepb >= 0 and stepb <= 100:
                return (stepsax, stepb)
    return None


with open("test.txt") as f:

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
            sum += solution[0] * 3 + solution[1]

        print(solution)

        l = f.readline()
        if not l:
            break
    print(sum)
