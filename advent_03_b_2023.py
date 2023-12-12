import os
import re

day_03_input = "/inputs/03_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_03_input)


def get_gear(line):
    special_characters = re.compile('[*]')
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


def get_paralel_gear(sym_index, lines):
    prev, curr, step = lines
    gear_ratio = 0
    for num in sym_index:
        base = 1
        left = num - 1 if num - 1 >= 0 else None
        right = num + 1 if num + 1 <= 139 else None
        num_pad_1 = int(prev[left]) if left in prev else None
        num_pad_2 = int(prev[num]) if num in prev else None
        num_pad_3 = int(prev[right]) if right in prev else None
        num_pad_4 = int(curr[left]) if left in curr else None
        num_pad_6 = int(curr[right]) if right in curr else None
        num_pad_7 = int(step[left]) if left in step else None
        num_pad_8 = int(step[num]) if num in step else None
        num_pad_9 = int(step[right]) if right in step else None
        adjacent = list(set([
            num_pad_1, num_pad_2, num_pad_3, num_pad_4,
            num_pad_6, num_pad_7, num_pad_8, num_pad_9
          ]))
        clear = [x for x in adjacent if x is not None]
        if len(clear) > 1:
            for num in clear:
                base *= num
            gear_ratio += base
    return gear_ratio


with open(input_file, encoding="utf-8") as i_file:
    num_gears = []
    char_num = [[], []]
    for line in i_file:
        char_num[0].append(get_gear(line))
        char_num[1].append(get_nums(line))
    for ite in range(len(char_num[0])):
        previous = ite - 1 if ite - 1 >= 0 else ite
        foward = ite + 1 if ite + 1 < len(char_num[0]) else ite
        prev_line = char_num[1][previous]
        this_line = char_num[1][ite]
        next_line = char_num[1][foward]
        num_gears.append(
            get_paralel_gear(
                char_num[0][ite],
                [prev_line, this_line, next_line]
              )
            )
    print(sum(num_gears))
    i_file.close()
