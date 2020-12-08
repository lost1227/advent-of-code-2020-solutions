from pathlib import Path
import re


in_file = Path("./inputs.txt")

if not in_file.exists():
    print("Input not found")
    exit()
 

pattern = re.compile("(\d+)-(\d+) ([a-z]): (.*)")

valid_count = 0

with in_file.open("r") as f:
    for line in f.readlines():
        matches = pattern.fullmatch(line.strip())
        firstocc = int(matches.group(1))
        secondocc = int(matches.group(2))
        needle = matches.group(3)
        haystack = matches.group(4)
        
        first_cond = haystack[firstocc - 1] == needle
        second_cond = haystack[secondocc - 1] == needle
        
        if first_cond != second_cond:
            valid_count += 1
            print("[.] {}".format(line.strip()))
        else:
            print("[x] {}".format(line.strip()))

print("{} are valid".format(valid_count))