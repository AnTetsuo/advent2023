import os

day_02_input = "/inputs/02_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_02_input)


def parse_cubes(list_cubes):
    cubes = list_cubes.split(',')
    number_color = [x.strip() for x in cubes]
    pull = {}
    for cube in number_color:
        number, color = cube.split(' ')
        pull[color] = int(number)
    return pull


def dice_min_config(pulls):
    config = {}
    for pull in pulls:
        for color, quantity in pull.items():
            if color not in config:
                config[color] = int(quantity)
            else:
                config[color] = (
                    quantity if quantity > config[color] else config[color]
                  )
    return config.values()


def analyze_game(game):
    game_id, pulls = game.split(':')
    list_of_pulls = pulls.split(';')
    parsed_pulls = [parse_cubes(pull) for pull in list_of_pulls]
    return (int(game_id.split(' ')[1]), parsed_pulls)


with open(input_file, encoding="utf-8") as i_file:
    sum_of_power = 0
    for line in i_file:
        game_id, pulls = analyze_game(line)
        power = 1
        checks = []
        for dice in dice_min_config(pulls):
            power *= dice
        sum_of_power += power
    print(sum_of_power)
    i_file.close()
