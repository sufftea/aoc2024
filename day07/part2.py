def concat(a, b):
    a = str(a)
    b = str(b)

    return int(a + b)


def run(target, values, result):
    if not values:
        return result == target

    if run(target, values[1:], result * values[0]):
        return True
    if run(target, values[1:], result + values[0]):
        return True
    if run(target, values[1:], concat(result, values[0])):
        return True
    return False


with open("input.txt") as f:
    sum = 0

    for equation in f:
        (result, values) = equation.split(": ")
        result = int(result)
        values = list(map(int, values.split(" ")))

        print((result, values), end="  --  ")

        solvable = run(result, values[1:], values[0])

        print(solvable)

        if solvable:
            sum += result

    print(sum)
