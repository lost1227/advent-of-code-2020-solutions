from pathlib import Path

in_file = Path("./inputs.txt")

if not in_file.exists():
    print("Input not found")
    exit()

groups = []
curr = ""

with in_file.open("r") as f:
    for line in f.readlines():
        clean_line = line.strip()
        if len(clean_line) == 0:
            groups.append("".join(set(curr)))
            curr = ""
        else:
            curr += clean_line

groups.append("".join(set(curr)))

total = 0
for group in groups:
    total += len(group)

print(groups)
print("Total:", total)