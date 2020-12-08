from pathlib import Path

in_file = Path("./inputs.txt")

if not in_file.exists():
    print("Input not found")
    exit()

passports = []
curr = {}
with in_file.open("r") as f:
    for line in f.readlines():
        clean_line = line.strip()
        if len(clean_line) == 0:
            passports.append(curr)
            curr = {}
        else:
            for entry in clean_line.split(" "):
                split_entry = entry.split(":")
                if(len(split_entry) != 2):
                    print("Invalid entry: {}".format(entry))
                else:
                    key = split_entry[0]
                    value = split_entry[1]
                    curr[key] = value

passports.append(curr)

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_passports = 0

for passport in passports:
    valid = True
    for key in required_keys:
        if key not in passport:
            valid = False
            break
    if valid:
        valid_passports += 1

print(valid_passports)