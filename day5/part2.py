from pathlib import Path

in_file = Path("./inputs.txt")

if not in_file.exists():
    print("Input not found")
    exit()

plane = []
for i in range(128):
    plane.append([ None ] * 8)

with in_file.open("r") as f:
    for line in f.readlines():
        clean_line = line.strip()
        if len(clean_line) != 10:
            print("Invalid line:", clean_line)
        else:
            start = 0
            end = len(plane)
            for i in range(0, 7):
                mid = (start + end) // 2
                if clean_line[i] == 'F':
                    end = mid
                elif clean_line[i] == 'B':
                    start = mid
                else:
                    print("Invalid line:", clean_line)
                    exit()
            if start != end - 1:
                print("Could not find row")
                exit()
            row = start
            start = 0
            end = len(plane[row])
            for i in range(7, 10):
                mid = (start + end) // 2
                if clean_line[i] == 'L':
                    end = mid
                elif clean_line[i] == 'R':
                    start = mid
                else:
                    print("Invalid line:", clean_line)
            if start != end - 1:
                print("Could not find seat")
                exit()
            seat = start
            print("Found row {} seat {} id {}".format(row, seat, (row * 8) + seat))
            plane[row][seat] = (row * 8) + seat

max_id = 0
my_seat = None
for i in range(1, (len(plane[0]) * len(plane)) - 1):
    curr = plane[i // 8][i % 8]
    prev = plane[(i - 1) // 8][(i - 1) % 8]
    nex = plane[(i + 1) // 8][(i + 1) % 8]
    if curr is not None and curr > max_id:
        max_id = curr
    if prev is not None and nex is not None and curr is None:
        my_seat = i
        
print(plane)

print("max_id: ", max_id)
print("my_seat: ", my_seat)
    