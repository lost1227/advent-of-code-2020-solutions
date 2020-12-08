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
# the obvoius O(n^3) algorithm is good enough
for i in range(0, len(expenses)):
    for j in range(i, len(expenses)):
        for k in range(j, len(expenses)):
            expense_sum = expenses[i] + expenses[j] + expenses[k]
            if expense_sum == 2020:
                print("{} + {} + {} = {}".format(
                    expenses[i], expenses[j], expenses[k], expense_sum
                ))
                print("{} * {} * {} = {}".format(
                    expenses[i], expenses[j], expenses[k],
                    expenses[i] * expenses[j] * expenses[k]
                ))
                print()