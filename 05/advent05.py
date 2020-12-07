afile = open("input05.txt", 'r')

sequences = []
for aline in afile:
    sequences.append(aline.strip())

start = 0

seat_ids = []

for sequence in sequences:
    numbers_rows = []
    num_rows = 128
    start = 0

    for i in range(num_rows):
        numbers_rows.append(i)
    for sequence_num in range(7):
        if sequence[sequence_num]== 'F':
            numbers_rows = numbers_rows[start:(num_rows//2)]
        if sequence[sequence_num]== 'B':
            numbers_rows = numbers_rows[(num_rows//2):num_rows]
        num_rows = num_rows//2

    numbers_cols = []
    num_cols = 8
    start = 0

    for i in range(num_cols):
        numbers_cols.append(i)

    for sequence_num in range(7, 10):
        if sequence[sequence_num]== 'L':
            numbers_cols = numbers_cols[start:(num_cols//2)]
        if sequence[sequence_num]== 'R':
            numbers_cols = numbers_cols[(num_cols//2):num_cols]
        num_cols = num_cols//2
    seat_ids.append(numbers_rows[0] * 8 + numbers_cols[0])


seat_ids.sort()
print(seat_ids)

check_range = 0
for i in range(89, 982):
    if seat_ids[check_range] != i:
        print(i)
    check_range = check_range + 1