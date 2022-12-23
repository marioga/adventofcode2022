from pathlib import Path


if __name__ == '__main__':
    total_contained = 0
    total_overlap = 0
    with Path('d4_input.txt').open() as f:
        for row in f:
            line = row.strip()
            r1, r2 = line.split(',')
            s1, e1 = map(int, r1.split('-'))
            s2, e2 = map(int, r2.split('-'))
            assert(s1 <= e1 and s2 <= e2)
            if (s1 <= s2 and e2 <= e1) or (s2 <= s1 and e1 <= e2):
                total_contained += 1
                total_overlap += 1
            elif (s1 <= s2 <= e1) or (s1 <= e2 <= e1):
                total_overlap += 1

    print(total_contained)
    print(total_overlap)
