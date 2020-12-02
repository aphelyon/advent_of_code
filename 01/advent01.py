# afile = open("input.txt", 'r')
#
# list = []
# for aline in afile:
#     list.append(int(aline.strip()))
#
# dict = {}
#
# for number in list:
#     dict[number] = 1
#
# for number in list:
#     inverse = 2020 - number
#     try:
#         dict[inverse] = dict[inverse] + 1
#     except KeyError:
#         pass
#
# for number in list:
#     inverse = 2020 - number
#     try:
#         if dict[inverse] == 2:
#             print(inverse, number)
#     except KeyError:
        pass

afile = open("input.txt", 'r')

list = []
for aline in afile:
    list.append(int(aline.strip()))

dict = {}
dict2 = {}

for number in list:
    dict[number] = 1

for number in list:
    inverse = 2020 - number
    try:
        dict2[inverse] = 1
    except KeyError:
        pass

all_addition_list = []
sum_dict = {}

for numbera in list:
    for numberb in list:
        if numbera != numberb:
            all_addition_list.append(numbera + numberb)
            sum_dict[numbera + numberb] = (numbera, numberb)


print(all_addition_list)
for number in all_addition_list:
    try:
        if number in dict2.keys():
            print(number)
            print(sum_dict[number])
    except KeyError:
        pass