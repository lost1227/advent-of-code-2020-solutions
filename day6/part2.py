from pathlib import Path

in_file = Path("./inputs.txt")

if not in_file.exists():
    print("Input not found")
    exit()

groups = []
first_line = True
curr = set()

with in_file.open("r") as f:
    for line in f.readlines():
        clean_line = line.strip()
        if len(clean_line) == 0:
            groups.append(curr)
            curr = set()
            first_line = True
        elif first_line:
            curr = set(clean_line)
            first_line = False
        else:
            curr = curr.intersection(set(clean_line))

groups.append(curr)

total = 0
for group in groups:
    total += len(group)

print(groups)
print("Total:", total)