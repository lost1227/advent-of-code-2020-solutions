from pathlib import Path

in_file = Path("./inputs.txt")

if not in_file.exists():
    print("Input not found")
    exit()

trees = 0

pos = 0

with in_file.open("r") as f:
    for line in f.readlines():
        if y % dy != 0:
            y += 1
            continue
        clean_line = line.strip()
        line_pos = pos % len(clean_line)
        if clean_line[line_pos] == '#':
            trees += 1
        pos += 3

print("Hit {} trees".format(trees))