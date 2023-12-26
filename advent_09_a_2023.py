import os


def checker(seq):
    return [True if x == 0 else False for x in seq]


def difference_checker(sequence):
    parsed_seq = [int(x) for x in sequence]
    check = checker(parsed_seq)
    history_diff = []
    while True:
        zeros = []
        for ind, x in enumerate(parsed_seq):
            if ind == len(parsed_seq) - 1:
                break
            diff = parsed_seq[ind + 1] - x
            zeros.append(diff)
        history_diff.append(zeros)
        parsed_seq = zeros
        check = checker(zeros)
        if all(check):
            break
    return [[int(x) for x in sequence], *history_diff]


def aggregate_diff(diff_hist):
    sequence, *hist = diff_hist
    next_diff = sum([x[-1] for x in hist])
    next_ele = sequence[-1] + next_diff
    return next_ele


day_09_input = "/inputs/09_test.txt"
input_path = os.getcwd()
input_file = input_path + str(day_09_input)

with open(input_file, encoding="utf-8") as i_file:
    history = i_file.readlines()
    strip_split = [x.strip().split(' ') for x in history]
    difference = [difference_checker(sequence) for sequence in strip_split]
    next_value = [aggregate_diff(x) for x in difference]
    print(sum(next_value))
    i_file.close()
