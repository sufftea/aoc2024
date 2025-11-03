
def is_safe(levels, skipped = False):
    prev = levels[0]
    increasing = ( levels[0] - levels[1] ) < 0

    for i, curr in enumerate(levels[1:]):
        diff = curr - prev

        problem = False
        if abs(diff) < 1 or abs(diff) > 3:
            problem = True
        if increasing and diff < 0 or not increasing and diff > 0:
            problem = True


        if problem:
            if not skipped:
                a = is_safe([l for j, l in enumerate(levels) if j != i], skipped=True)
                b = is_safe([l for j, l in enumerate(levels) if j != i + 1], skipped=True)
                c = False
                if i >= 1:
                    c = is_safe([l for j, l in enumerate(levels) if j != i - 1], skipped=True)
                return a or b or c
            else:
                return False
        prev = curr

    return True

with open('input.txt') as f:
    nof_safe = 0
    for report in f:
        levels = [int(r) for r in report.split(' ') ]

        safe = is_safe(levels, False)
        if safe:
            nof_safe += 1

        print(f'{safe}: {levels}')

    # print(f'min: {min_count}; max: {max_count}')
    print(nof_safe)

