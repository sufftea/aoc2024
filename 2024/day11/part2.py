def get_adjacents(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        a = s[: len(s) // 2]
        b = s[len(s) // 2 :]

        return [int(a), int(b)]

    else:
        return [stone * 2024]


class SparseMat:
    def __init__(self, stones) -> None:
        self._map = {s: {} for s in stones}

    def set(self, i, j, value):
        self._map.update({i: {j: value}})

    def get(self, i, j):
        return self._map.get(i, {j: 1 for j in get_adjacents(i)}).get(j, 0)

    def get_non_zero_indexes(self):
        return list(self._map.keys())

    def get_row(self, i):
        result = self._map.get(i, {})

        for adj in get_adjacents(i):
            if adj not in result:
                result[adj] = 1

        return result

    def get_column(self, j):
        # result = self._map.get(i, {})
        result = {}

        for row in self._map.values():
            if j in row:
                result[j] = row[j]

        for adj in get_adjacents(j):
            if adj not in result:
                result[adj] = 1

        return result


with open("test.txt") as f:
    input = list(map(int, f.read().split(" ")))

    mat = SparseMat(input)

    for _ in range(0, 6):
        next_mat = SparseMat([])

        non_zeroes = mat.get_non_zero_indexes()
        for i in non_zeroes:
            for j in non_zeroes:
                sum = 0
                for k in non_zeroes:
                    a = mat.get(i, k)
                    b = mat.get(k, j)
                    sum += a * b
                next_mat.set(i, j, sum)

        mat = next_mat

    result = 0
    for stone in input:
        __import__("pprint").pprint(mat._map[stone])
