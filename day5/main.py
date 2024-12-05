def check_update(pages, rules):
    all_pages = set(pages)
    prev_pages = set()
    for page in pages:
        if page not in rules:
            prev_pages.add(page)
            continue
        for rule in rules[page]:
            if rule in all_pages and rule not in prev_pages:
                return False

        prev_pages.add(page)

    return True


def rec(page, fixed, skip_indexes, prev_pages, all_pages, rules):
    if page in rules:
        for rule in rules[page]:
            if rule in all_pages and rule not in prev_pages:
                rec(rule, fixed, skip_indexes, prev_pages, all_pages, rules)

                prev_pages.add(rule)
                fixed.append(rule)
                skip_indexes.add(all_pages[rule])


def fix_update(pages, rules):
    fixed = []

    all_pages = {}
    for i, page in enumerate(pages):
        all_pages[page] = i

    skip_indexes = set()
    prev_pages = set()

    for i, page in enumerate(pages):
        if i in skip_indexes:
            continue

        rec(page, fixed, skip_indexes, prev_pages, all_pages, rules)

        prev_pages.add(page)
        fixed.append(page)

    return fixed


with open("input.txt") as o:
    rules = {}

    for rule in o:
        if rule == "\n":
            break

        [a, b] = map(int, rule.split("|"))

        if b in rules:
            rules[b].append(a)
        else:
            rules[b] = [a]

    sum = 0

    for update in o:
        pages = list(map(int, update.split(",")))

        if not check_update(pages, rules):
            fixed = fix_update(pages, rules)
            sum += fixed[int(len(fixed) / 2)]

    print(sum)
