def run(result, values):
    if len(values) == 1:
        return result == values[0]
    if run(result / values[-1], values[:-1]):
        return True
    if run(result - values[-1], values[:-1]):
        return True
    return False


with open("test.txt") as f:
    sum = 0
    for equation in f:
        (result, values) = equation.split(": ")
        result = int(result)
        values = list(map(int, values.split(" ")))

        print((result, values), end="  --  ")

        solvable = run(result, values)

        print(solvable)

        if solvable:
            sum += result

    print(sum)


# 10: 8 2
# 8: 8
