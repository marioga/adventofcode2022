import heapq
from pathlib import Path

if __name__ == '__main__':
    best = []

    with Path('d1_input.txt').open() as f:
        running_sum = 0
        for row in f:
            if line := row.strip():
                running_sum += int(line)
            else:
                if len(best) < 3:
                    heapq.heappush(best, running_sum)
                elif running_sum > best[0]:
                    heapq.heappushpop(best, running_sum)
                running_sum = 0

    print(best)
    print(sum(best))

