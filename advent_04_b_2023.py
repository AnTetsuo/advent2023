import os


day_01_input = "/inputs/04_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_01_input)


def parse_cards(line):
    house_pulls, client_pulls = line.split('|')
    card, win_nums = house_pulls.split(':')
    card_id = card[4:].strip()
    client_nums = [int(x) for x in client_pulls.strip().split(' ') if x != '']
    house_nums = [int(x) for x in win_nums.strip().split(' ') if x != '']
    return {'id': int(card_id) - 1,
            'client': client_nums,
            'house': house_nums,
            'units': 1}


with open(input_file, encoding="utf-8") as i_file:
    pile = [parse_cards(line) for line in i_file]
    for card in pile:
        for copies in range(card['units']):
            match = [True for x in card['house'] if x in card['client']]
            inc_units_ind = [ind for ind, x in enumerate(match)]
            for index in inc_units_ind:
                pile[card['id'] + index + 1]['units'] += 1
    print(sum([card['units'] for card in pile]))
    i_file.close()
