# afile = open("input02.txt", 'r')
#
# list = []
# for aline in afile:
#     list.append(aline.strip().split())
#
# print(list)
#
# count = 0
# for password in list:
#     numbers = password[0].split("-")
#     min = int(numbers[0])
#     max = int(numbers[1])
#
#     letter = password[1][0]
#
#     letter_count = 0
#     word = password[2]
#     for characters in word:
#         if characters == letter:
#             letter_count = letter_count + 1
#
#     if letter_count <= max and letter_count >= min:
#         count = count + 1
#
#
# print(count)

afile = open("input02.txt", 'r')

list = []
for aline in afile:
    list.append(aline.strip().split())

print(list)

count = 0
for password in list:
    numbers = password[0].split("-")
    min = int(numbers[0])
    max = int(numbers[1])

    letter = password[1][0]
    word = password[2]
    xor_count = 0

    if (word[min-1] == letter) ^ (word[max-1] == letter):
        count = count + 1

print(count)