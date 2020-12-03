# def reset_bounds(col):
#     return col - col_count
#
# afile = open("input03.txt", 'r')
#
# list_of_lists = []
# for aline in afile:
#     list_of_lists.append(aline.strip())
#
# row_count = len(list_of_lists)
#
# col_count = len(list_of_lists[0])
# count = 0
#
#
# current_col = 0
# for row in range(1, row_count):
#     print(list_of_lists[row])
#     current_col = current_col + 3
#
#     if current_col >= col_count:
#         current_col = reset_bounds(current_col)
#
#     if list_of_lists[row][current_col] == '#':
#         count = count + 1


def reset_bounds(col):
    return col - col_count

afile = open("input03.txt", 'r')

list_of_lists = []
for aline in afile:
    list_of_lists.append(aline.strip())

row_count = len(list_of_lists)

col_count = len(list_of_lists[0])




def get_slope(col_diff, row_diff):
    count = 0
    current_col = 0

    for row in range(row_diff, row_count, row_diff):
        print(list_of_lists[row])
        current_col = current_col + col_diff

        if current_col >= col_count:
            current_col = reset_bounds(current_col)

        if list_of_lists[row][current_col] == '#':
            count = count + 1

    return count

print( get_slope(1,1) * get_slope(3,1) * get_slope(5,1)  * get_slope(7,1) * get_slope(1,2) )