from dataclasses import dataclass, field


@dataclass
class Trie:
    char: str
    children: dict[str, "Trie"] = field(default_factory=lambda: {})
    is_final: bool = False

    def insert_sequence(self, sequence: str):
        if not sequence:
            return
        next_char = sequence[0]
        if next_char not in self.children:
            self.children[next_char] = Trie(char=next_char)

        next = self.children[next_char]
        next.is_final |= len(sequence) == 1

        next.insert_sequence(sequence[1:])


def create_trie(towels: list[str]) -> Trie:
    root = Trie(char="")

    for t in towels:
        root.insert_sequence(t)

    return root


mem: dict[tuple[int, str], int] = {}


def solve_patterns(trie_root, curr_child, pattern, matches: list[str]) -> int:
    prev = mem.get((id(curr_child), pattern), None)
    if prev is not None:
        return prev

    if not pattern:
        return 1 if curr_child.is_final else 0

    count = 0

    next_child = curr_child.children.get(pattern[0], None)
    if next_child is not None:
        count += solve_patterns(trie_root, next_child, pattern[1:], matches)

    if curr_child.is_final:
        count += solve_patterns(trie_root, trie_root, pattern, matches)

    mem[(id(curr_child), pattern)] = count
    return count


with open("input.txt") as f:
    towels = f.readline()[:-1].split(", ")

    trie = create_trie(towels)

    f.readline()

    solvables = 0
    for pattern in f:
        pattern = pattern[:-1]

        solution = []
        result = solve_patterns(trie, trie, pattern, solution)
        print(f"{result} \t for pattern: {pattern} \t solution: {solution}")
        solvables += result
    print(solvables)
