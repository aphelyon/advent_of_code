import re

# afile = open("input04.txt", 'r')
# passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# passports = []
# passport = {}
#
# valid_passport_count = 0
#
# passport_list = afile.read().strip().split("\n")
#
# fields = []
# for passport_field in passport_list:
#     if ' ' in passport_field:
#         multi_field_passport_field = passport_field.split(' ')
#
#         for field in multi_field_passport_field:
#             fields.append(field)
#     else:
#        fields.append(passport_field)
#
# fields.append('')
#
# for item in fields:
#     if item != '':
#         passport_item = item.split(':')
#         passport_key = passport_item[0]
#         passport_value = passport_item[1]
#         passport[passport_key] = passport_value
#
#     else:
#         field_count = 0
#
#         for field in passport_fields:
#             if field in passport.keys():
#                 field_count = field_count + 1
#
#         if field_count == len(passport_fields):
#             valid_passport_count = valid_passport_count + 1
#
#         passport = {}

afile = open("input04.txt", 'r')
passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passports = []
passport = {}

valid_passport_count = 0

passport_list = afile.read().strip().split("\n")

fields = []
for passport_field in passport_list:
    if ' ' in passport_field:
        multi_field_passport_field = passport_field.split(' ')

        for field in multi_field_passport_field:
            fields.append(field)
    else:
       fields.append(passport_field)

fields.append('')

for item in fields:
    if item != '':
        passport_item = item.split(':')
        passport_key = passport_item[0]
        passport_value = passport_item[1]
        passport[passport_key] = passport_value

    else:
        try:
            field_count = 0
            year_matcher = re.compile('^[0-9]{4}$')
            if "byr" in passport and year_matcher.match(passport["byr"]) and int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002:
                field_count = field_count + 1

            if "iyr" in passport and year_matcher.match(passport["iyr"]) and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020:
                field_count = field_count + 1

            if "eyr" in passport and year_matcher.match(passport["eyr"]) and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030:
                field_count = field_count + 1

            height_matcher = re.compile('^[0-9]+(cm|in)$')

            if "hgt" in passport and (height_matcher.match(passport["hgt"]) and "cm" in passport["hgt"] and int(passport["hgt"].replace("cm", "")) >= 150 and int(passport["hgt"].replace("cm", "")) <= 193) or \
                    (height_matcher.match(passport["hgt"]) and "in" in passport["hgt"] and int(passport["hgt"].replace("in", "")) >= 59 and int(passport["hgt"].replace("in", "")) <= 76):
                field_count = field_count + 1


            hair_color_matcher = re.compile('^#(([0-9]|[a-f]){6})$')
            if "hcl" in passport and hair_color_matcher.match(passport["hcl"]):
                field_count = field_count + 1


            eye_color_matcher = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')

            if "ecl" in passport and eye_color_matcher.match(passport["ecl"]):
                field_count = field_count + 1

            pid_matcher = re.compile('^[0-9]{9}$')

            if "pid" in passport and pid_matcher.match(passport["pid"]):
                field_count = field_count + 1

        except KeyError:
            pass

        if field_count == len(passport_fields):
            valid_passport_count = valid_passport_count + 1

        passport = {}
