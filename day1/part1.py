from pathlib import Path

in_file = Path("./inputs.txt")

if not in_file.exists():
    print("Input not found")
    exit()

expenses = []

with in_file.open("r") as f:
    for line in f.readlines():
        expenses.append(int(line.strip()))
        
# There are only 200 lines, why bother implementing some fancy algorithm if
# the obvoius O(n^2) algorithm is good enough


for i, expense1 in enumerate(expenses):
    for j, expense2 in enumerate(expenses):
        if i != j:
            if expense1 + expense2 == 2020:
                print("{} + {} = {}".format(
                    expense1, expense2, expense1 + expense2
                ))
                print("{} * {} = {}".format(
                    expense1, expense2, expense1 * expense2
                ))
                print()