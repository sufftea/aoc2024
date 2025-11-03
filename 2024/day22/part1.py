def next_secret(n):
    n = ((n << 6) ^ n) & ((1 << 24) - 1)
    n = (n >> 5) ^ n
    n = ((n << 11) ^ n) & ((1 << 24) - 1)

    return n


with open("input.txt") as f:

    sum = 0
    for secret_number in f:
        secret_number = int(secret_number[:-1])

        for _ in range(2000):
            secret_number = next_secret(secret_number)
        print(secret_number)

        sum += secret_number
    print(f"sum = {sum}")
