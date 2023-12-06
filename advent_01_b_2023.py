import os
import re


def filter_numbers(characters):
    num_strings = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine'
      ]

    filter_str = [num for num in num_strings if num in characters]
    filter_num = [char for char in characters if char.isnumeric()]
    filtered = [*filter_num, *filter_str]
    occurrences = {}

    for value in set(filtered):
        match = re.finditer(value, characters)
        for number in match:
            numeric = number.group().isnumeric()
            ref = int(number.group()) if numeric else (
                num_strings.index(number.group())
              )
            if ref not in occurrences:
                occurrences[ref] = [number.start()]
            else:
                occurrences[ref].append(number.start())
            occurrences[ref].sort()
    return occurrences


day_01_input = "/inputs/01_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_01_input)


with open(input_file, encoding="utf-8") as i_file:
    sum_coordinates = 0
    for line in i_file:
        first = [1000, 0]
        last = [-1, 0]
        coordinates = filter_numbers(line)
        for props, value in coordinates.items():
            if value[0] < first[0]:
                first[0] = value[0]
                first[1] = props
            if value[-1] > last[0]:
                last[0] = value[-1]
                last[1] = props
        concat_1 = str(first[1])
        concat_2 = str(last[1])
        sum_coordinates += int(concat_1 + concat_2)
    print(sum_coordinates)
    i_file.close()
