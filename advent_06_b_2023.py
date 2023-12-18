import os

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
    raw_time, raw_distance = i_file.readlines()
    time = int(''.join([x for x in raw_time.split()[1:]]))
    distance = int(''.join([x for x in raw_distance.split()[1:]]))
    min_max_speed = min_max_speed(time, distance)
    records = len(range(min_max_speed[0], min_max_speed[1] + 1))
    print(records)
    i_file.close()
