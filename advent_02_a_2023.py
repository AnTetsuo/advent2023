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


def validate_pull(pull):
    config = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    valid = [pull[x] > config[x] for x in pull]
    return valid


def analyze_game(game):
    game_id, pulls = game.split(':')
    list_of_pulls = pulls.split(';')
    parsed_pulls = [parse_cubes(pull) for pull in list_of_pulls]
    return (int(game_id.split(' ')[1]), parsed_pulls)


with open(input_file, encoding="utf-8") as i_file:
    sum_of_valid_games = 0
    for line in i_file:
        game_id, pulls = analyze_game(line)
        checks = []
        for pull in pulls:
            validate = any(validate_pull(pull))
            checks.append(validate)
            if validate:
                break
        if any(checks):
            continue
        else:
            sum_of_valid_games += int(game_id)
    print(sum_of_valid_games)
    i_file.close()
