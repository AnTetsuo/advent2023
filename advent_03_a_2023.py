import os
import re

day_03_input = "/inputs/03_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_03_input)


def get_symbols(line):
    special_characters = re.compile('[^a-zA-Z0-9.\\s]')
    match = re.finditer(special_characters, line)
    special_char_pos = []
    if match is None:
        return None
    else:
        [special_char_pos.append(x.start()) for x in match]
        return special_char_pos


def get_nums(line):
    num = re.compile('[0-9]')
    match = re.finditer(num, line)
    num_position = {}
    if match is None:
        return None
    else:
        pos_char = [[x.start(), x.group()] for x in match]
        for curr in range(len(pos_char)):
            foward = curr + 1 if curr + 1 <= len(pos_char) - 1 else curr
            two_foward = curr + 2 if curr + 2 < len(pos_char) else curr
            current = pos_char[curr]
            step = pos_char[foward]
            step_two = pos_char[two_foward]

            if current[0] in num_position:
                continue

            if current[0] + 1 == step[0] and current[0] + 2 == step_two[0]:
                num_position[current[0]] = current[1] + step[1] + step_two[1]
                num_position[step[0]] = current[1] + step[1] + step_two[1]
                num_position[step_two[0]] = current[1] + step[1] + step_two[1]
                continue

            if current[0] + 1 == step[0]:
                num_position[current[0]] = current[1] + step[1]
                num_position[step[0]] = current[1] + step[1]
                continue

            num_position[current[0]] = current[1]
        return num_position


def overlap_char_num(indexes, nums):
    num_parts = []
    for each in indexes:
        step = each + 1
        curr = each in nums
        prev = each - 1 if each - 1 > 0 else None
        if curr is True:
            num_parts.append(nums[each])
            continue
        if prev in nums:
            num_parts.append(nums[prev])
        if step in nums:
            num_parts.append(nums[step])
            continue
    return num_parts


with open(input_file, encoding="utf-8") as i_file:
    num_parts = []
    char_num = [[], []]
    for line in i_file:
        char_num[0].append(get_symbols(line))
        char_num[1].append(get_nums(line))
    for ite in range(len(char_num[0])):
        previous = ite - 1 if ite - 1 >= 0 else ite
        foward = ite + 1 if ite + 1 < len(char_num[0]) else ite
        prev_line = overlap_char_num(char_num[0][ite], char_num[1][previous])
        this_line = overlap_char_num(char_num[0][ite], char_num[1][ite])
        next_line = overlap_char_num(char_num[0][ite], char_num[1][foward])
        num_parts = [*num_parts, *this_line, *next_line, *prev_line]
    number = [int(x) for x in num_parts]
    print(sum(number))
    i_file.close()
