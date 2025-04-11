from collections import deque


def calculate_next_secret(n):
    n = ((n << 6) ^ n) & ((1 << 24) - 1)
    n = (n >> 5) ^ n
    n = ((n << 11) ^ n) & ((1 << 24) - 1)

    return n


def solve(secret_numbers):

    sequences = {}

    for secret in secret_numbers:
        visited = set()
        last_changes = deque()

        for _ in range(2000):
            prev_secret = secret
            next_secret = calculate_next_secret(secret)

            prev_cost = prev_secret % 10
            next_cost = next_secret % 10
            change = next_cost - prev_cost

            last_changes.append(change)
            if len(last_changes) > 3:

                sequence = tuple(last_changes)

                if sequence not in visited:
                    visited.add(sequence)

                    sum = sequences.get(sequence, 0)
                    sequences[sequence] = sum + next_cost

                last_changes.popleft()
            secret = next_secret

    values = list(sequences.values())
    values.sort(reverse=True)
    return values[0]


with open("input.txt") as f:

    secret_numbers = f.read().split("\n")[:-1]
    secret_numbers = list(map(int, secret_numbers))
    solution = solve(secret_numbers)
    print(solution)
