from pathlib import Path


def get_priority(elem):
    if elem == elem.lower():
        return ord(elem) - ord('a') + 1
    return ord(elem) - ord('A') + 27


if __name__ == '__main__':
    priority_sum = 0
    with Path('d3_input.txt').open() as f:
        common_for_triple = None
        for i, row in enumerate(f):
            line = row.strip()
            if i % 3 == 0:
                common_for_triple = set(line)
            else:
                common_for_triple &= set(line)

            if i % 3 == 2:
                assert(len(common_for_triple) == 1)
                elem = next(iter(common_for_triple))
                priority_sum += get_priority(elem)

    print(priority_sum)

