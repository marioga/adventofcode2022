from pathlib import Path


def get_priority(elem):
    if elem == elem.lower():
        return ord(elem) - ord('a') + 1
    return ord(elem) - ord('A') + 27


if __name__ == '__main__':
    priority_sum = 0
    with Path('d3_input.txt').open() as f:
        for row in f:
            line = row.strip()
            _len = len(line)
            assert(_len % 2 == 0)
            h1, h2 = line[:_len // 2], line[_len // 2:]
            common = set(h1) & set(h2)
            assert(len(common) == 1)
            elem = next(iter(common))
            priority_sum += get_priority(elem)
    print(priority_sum)

