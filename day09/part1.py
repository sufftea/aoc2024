def run(file_map):
    result = []
    nof_files = int(len(file_map) / 2)

    s = 0
    e = nof_files - 1
    # end_file_space = file_map[e * 2]
    while s < e:
        file_space = file_map[s * 2]
        free_space = file_map[s * 2 + 1]

        result += [s] * file_space

        while free_space > 0 and e > s:
            end_blocks_to_insert = min(file_map[e * 2], free_space)

            result += [e] * end_blocks_to_insert
            # print("".join(map(str, result)))

            free_space -= end_blocks_to_insert
            file_map[e * 2] -= end_blocks_to_insert
            if file_map[e * 2] == 0:
                e -= 1

        s += 1

    result += [s] * file_map[s * 2]

    return result


with open("input.txt") as f:
    input = f.read()
    input = list(map(int, input[:-1]))
    if len(input) % 2 != 0:
        input += [0]

    is_file = True

    # for i, n in enumerate(input):
    #     if is_file:
    #         print(str(int(i / 2)) * n, end="")
    #     else:
    #         print("." * n, end="")
    #     is_file = not is_file
    # print()

    reduced = run(input)

    # print("".join(map(str, reduced)))

    result = 0
    for i, file in enumerate(reduced):
        result += i * file
    print(result)
