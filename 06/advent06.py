# afile = open("input06.txt", 'r')
#
# valid_passport_count = 0
#
# customs_list = afile.read().strip().split("\n")
#
# customs_list.append('')
#
# question_dict = {}
# question_count = []
#
# for questions in customs_list:
#     if questions != '':
#         for letter in questions:
#             question_dict[letter] = 1
#     else:
#         question_count.append((len(question_dict)))
#         question_dict = {}
#
# print(sum(question_count))

afile = open("input06.txt", 'r')

valid_passport_count = 0

customs_list = afile.read().strip().split("\n")

customs_list.append('')

question_dict = {}
question_count = []

count = 0

for questions in customs_list:
    if questions != '':
        count = count + 1
        for letter in questions:
            if letter not in question_dict:
                question_dict[letter] = 1
            else:
                question_dict[letter] = question_dict[letter] + 1


    else:
        everyone_count = 0
        for key in question_dict.keys():
            if question_dict[key] == count:
                everyone_count = everyone_count + 1
        question_count.append(everyone_count)

        question_dict = {}
        count = 0

print(sum(question_count))