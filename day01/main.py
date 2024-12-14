from typing import Counter

right = []
left = []
with open("input.txt") as f:

    for line in f:
        [a, b] = line.split("   ")
        print(f"a: {a}; b: {b}")
        left.append(int(a))
        right.append(int(b))

right.sort()
left.sort()

rc = Counter(right)
sum = 0
for n in left:
    if n in rc:
        sum += n * rc[n]

print(sum)
