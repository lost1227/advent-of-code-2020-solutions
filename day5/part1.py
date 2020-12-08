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
for row in plane:
    for seat in row:
        if seat is not None and seat > max_id:
            max_id = seat

print(plane)
print("Max id", max_id)