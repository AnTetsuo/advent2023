import os
from functools import reduce

day_06_input = "/inputs/06_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_06_input)


def min_max_speed(time, distance):
    min_startup = 1
    max_buildup = 1
    while True:
        if min_startup * (time - min_startup) <= distance:
            min_startup += 1
            continue
        break
    while True:
        curr_startup = time - max_buildup
        completion_time = distance / curr_startup
        if completion_time >= time - curr_startup:
            max_buildup += 1
            continue
        break
    return (min_startup, time - max_buildup)


with open(input_file, encoding="utf-8") as i_file:
    sum_coordinates = 0
    raw_time, raw_distance = i_file.readlines()
    time = [int(x) for x in raw_time.split()[1:]]
    distance = [int(x) for x in raw_distance.split()[1:]]
    min_max_speed = [min_max_speed(x, distance[ind]) for
                     ind, x in enumerate(time)]
    possible_records = [len(range(x[0], x[1] + 1)) for x in min_max_speed]
    product = reduce(lambda x, y: x * y, possible_records, 1)
    print(product)
    i_file.close()
