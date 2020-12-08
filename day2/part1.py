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
        minocc = int(matches.group(1))
        maxocc = int(matches.group(2))
        needle = matches.group(3)
        haystack = matches.group(4)
        
        occ = haystack.count(needle)
        
        if occ >= minocc and occ <= maxocc:
            valid_count += 1
            print("[.] {}".format(line.strip()))
        else:
            print("[x] {}".format(line.strip()))

print("{} are valid".format(valid_count))