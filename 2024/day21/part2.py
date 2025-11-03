import heapq
from dataclasses import dataclass, field, replace

ROBOT_BUTTONS = {
    # (0, 0): "X",
    (1, 0): "^",
    (2, 0): "A",
    (0, 1): "<",
    (1, 1): "v",
    (2, 1): ">",
}


NUMPAD_BUTTONS = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    #
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    #
    (0, 2): "1",
    (1, 2): "2",
    (2, 2): "3",
    #
    # (0, 3): "X",
    (1, 3): "0",
    (2, 3): "A",
}

ACTION_TO_OFFSET = {
    "A": (0, 0),
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}

MOVE_ACTIONS = {"<", ">", "v", "^"}

NUMPAD_BUTTON_TO_COORDS = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    #
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    #
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    #
    # "X": (0, 3),
    "0": (1, 3),
    "A": (2, 3),
}


def _move(curr: tuple[int, int], offset: tuple[int, int]):
    return tuple(a + b for a, b in zip(curr, offset))


@dataclass(order=True, frozen=True)
class State:
    remaining_code: str

    arms: tuple[tuple[int, int], ...] = tuple([(2, 0) for _ in range(25)] + [(2, 3)])
    # arms: list[tuple[int, int]] = field(
    #     default_factory=lambda: [(2, 0) for _ in range(2)] + [(2, 3)]
    # )
    # arm_a: tuple[int, int] = (2, 3)
    # arm_b: tuple[int, int] = (2, 0)
    # arm_c: tuple[int, int] = (2, 0)
    sequence: str = field(compare=False, hash=False, default="")

    def apply_action(self, action: str) -> "State | None":
        result = replace(self, sequence=self.sequence + action)

        arms = list(self.arms)
        for i, arm in enumerate(arms[:-1]):
            if action in MOVE_ACTIONS:
                next_arm_state = _move(arm, ACTION_TO_OFFSET[action])

                if next_arm_state not in ROBOT_BUTTONS:
                    return None

                arms[i] = next_arm_state
                return replace(result, arms=tuple(arms))

            action = ROBOT_BUTTONS[arm]

        last_arm = arms[-1]

        if action in MOVE_ACTIONS:
            next_arm_state = _move(last_arm, ACTION_TO_OFFSET[action])

            if next_arm_state not in NUMPAD_BUTTONS:
                return None

            arms[-1] = next_arm_state
            return replace(result, arms=tuple(arms))

        numpad_code = NUMPAD_BUTTONS[last_arm]
        if self.remaining_code[0] == numpad_code:
            return replace(result, remaining_code=self.remaining_code[1:])
        else:
            return None

    def get_neis(self):
        actions = [
            "A",
            "<",
            ">",
            "^",
            "v",
        ]

        neis = []
        for action in actions:
            pass
            nei = self.apply_action(action)
            neis.append(nei)

        return neis


def calculate_heuristic(s: State):
    if s.remaining_code == "":
        return 0
    tx, ty = NUMPAD_BUTTON_TO_COORDS[s.remaining_code[0]]
    sx, sy = s.arms[-1]
    dist = abs(tx - sx) + abs(ty - sy)

    remaining = len(s.remaining_code)

    return dist + remaining


def find_solution(code: str):
    to_visit = []
    heapq.heappush(to_visit, (0, 0, State(remaining_code=code)))

    visited = {}
    i = 0
    while to_visit:
        _, curr_cost, curr_state = heapq.heappop(to_visit)

        if curr_state.remaining_code == "":
            return curr_state

        old_cost = visited.get(curr_state, float("inf"))
        if curr_cost >= old_cost:
            continue
        visited[curr_state] = curr_cost

        if i % 1000 == 0:
            print(
                f"remaining: {curr_state.remaining_code} \t cost: {curr_cost} \t visited: {len(visited)} \t to_visit: {len(to_visit)}"
            )
        i += 1

        next_cost = curr_cost + 1
        for nei in curr_state.get_neis():
            if nei == None:
                continue

            old_cost = visited.get(nei, float("inf"))
            if next_cost >= old_cost:
                continue

            h = calculate_heuristic(nei)
            heapq.heappush(to_visit, (curr_cost + h, next_cost, nei))

    return None


def check_solution(expected_code: str, solution: str):
    s = State(remaining_code=expected_code)
    for i, action in enumerate(solution):
        s = s.apply_action(action)
        if s is None:
            return False
    return True


with open("input.txt") as f, open("test_answers.txt") as a:
    expected = a.read().split("\n")

    sum = 0
    for i, code in enumerate(f):
        code = code[:-1]

        solution = find_solution(code)
        if solution is None:
            print(f"solution for {code} is: None")
            continue

        print(f"solution for {code} is: {solution.sequence}")
        print(f"expected for {code} is: {expected[i]}")

        num_part = int(code[:-1])
        shortest_length = len(solution.sequence)

        sum += num_part * shortest_length

    print(sum)
