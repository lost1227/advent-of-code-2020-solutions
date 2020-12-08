from pathlib import Path
import re

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

height_pattern = re.compile("(\d*)(cm|in)")
def check_height(s):
    matches = height_pattern.fullmatch(s)
    if matches is None:
        return False
    height = int(matches.group(1))
    units = matches.group(2)
    if units == "cm":
        return height >= 150 and height <= 193
    elif units == "in":
        return height >= 59 and height <= 76
    else:
        return False

hcl_pattern = re.compile("#[0-9a-f]{6}")
cid_pattern = re.compile("\d{9}")

required_keys = {
    "byr" : lambda s : len(s) == 4 and int(s) >= 1920 and int(s) <= 2002,
    "iyr" : lambda s : len(s) == 4 and int(s) >= 2010 and int(s) <= 2020,
    "eyr" : lambda s : len(s) == 4 and int(s) >= 2020 and int(s) <= 2030,
    "hgt" : check_height,
    "hcl" : lambda s : hcl_pattern.fullmatch(s) is not None,
    "ecl" : lambda s : s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid" : lambda s : cid_pattern.fullmatch(s) is not None
}

valid_passports = 0

for passport in passports:
    valid = True
    for key, validator in required_keys.items():
        if key not in passport:
            valid = False
            break
        if not validator(passport[key]):
            print("failed {} validator".format(key))
            valid = False
            break
    if valid:
        print("[.] {}".format(passport))
        valid_passports += 1
    else:
        print("[x] {}".format(passport))

print(valid_passports)