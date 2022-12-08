from pathlib import Path

if __name__ == '__main__':
    with Path('d2_input.txt').open() as f:
        running_sum = 0
        for row in f:
            # 0 - rock, 1 - paper, 2 - scissors
            x, y = map(ord, row.strip().split())
            x -= ord('A')
            y -= ord('X')
            outcome = (y - x + 1) % 3
            # outcome: 0 -> 0 pts, 1 -> 3 pts, 2 -> 6 pts
            running_sum += (outcome * 3 + y + 1)

    print(running_sum)

