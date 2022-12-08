from pathlib import Path

if __name__ == '__main__':
    with Path('d2_input.txt').open() as f:
        running_sum = 0
        for row in f:
            # 0 - rock, 1 - paper, 2 - scissors
            x, outcome = map(ord, row.strip().split())
            x -= ord('A')
            outcome -= ord('X')
            y = (x + outcome - 1) % 3
            running_sum += (outcome * 3 + y + 1)

    print(running_sum)

