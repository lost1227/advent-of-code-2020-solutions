from pathlib import Path

in_file = Path("./inputs.txt")

if not in_file.exists():
    print("Input not found")
    exit()

def count_trees(dx, dy):
    trees = 0
    pos = 0
    y = 0
    with in_file.open("r") as f:
        for line in f.readlines():
            if y % dy != 0:
                y += 1
                continue
            clean_line = line.strip()
            line_pos = pos % len(clean_line)
            if clean_line[line_pos] == '#':
                trees += 1
            pos += dx
            y += 1
    return trees


trees = [
    count_trees(1, 1),
    count_trees(3, 1),
    count_trees(5, 1),
    count_trees(7, 1),
    count_trees(1, 2)
]

print("count_trees({}, {}): {}".format(1, 1, trees[0]))
print("count_trees({}, {}): {}".format(3, 1, trees[1]))
print("count_trees({}, {}): {}".format(5, 1, trees[2]))
print("count_trees({}, {}): {}".format(7, 1, trees[3]))
print("count_trees({}, {}): {}".format(1, 2, trees[4]))

print("{} * {} * {} * {} * {} = {}".format(
    trees[0],
    trees[1],
    trees[2],
    trees[3],
    trees[4],
    trees[0] * trees[1] * trees[2] * trees[3] * trees[4]
))