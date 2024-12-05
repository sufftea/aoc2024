kernels = [
    [
        "M.M",
        ".A.",
        "S.S",
    ],
    [
        "S.M",
        ".A.",
        "S.M",
    ],
    [
        "S.S",
        ".A.",
        "M.M",
    ],
    [
        "M.S",
        ".A.",
        "M.S",
    ],
]


def matches_kernel(field, kernel):
    # if len(kernel) > len(field) or len(kernel[0]) > len(field[0]):
    #     return False
    for x, kernel_row in enumerate(kernel):
        for y, match in enumerate(kernel_row):
            if len(field) > y and len(field[0]) > x:
                if match != "." and match != field[y][x]:
                    return False
            else:
                return False
    return True


with open("input.txt") as f:
    field = f.read().split("\n")[:-1]

    print(field)

    matches = 0
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            field_slice = [
                r[x : min(x + 3, len(r))] for r in field[y : min(len(field), y + 3)]
            ]
            if len(field_slice) == 0:
                continue
            for k in kernels:
                if matches_kernel(field_slice, k):
                    print(f"match:\n {field_slice}")
                    matches += 1

    print(matches)
