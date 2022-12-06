from pathlib import Path

if __name__ == '__main__':
    curr_max = 0

    with Path('d1_input.txt').open() as f:
        running_sum = 0
        for row in f:
            if line := row.strip():
                running_sum += int(line)
            else:
                curr_max = max(running_sum, curr_max)
                running_sum = 0

    curr_max = max(running_sum, curr_max)
    print(curr_max)

