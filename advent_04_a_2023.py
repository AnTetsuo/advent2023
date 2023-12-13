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
    return {'id': card_id, 'client': client_nums, 'house': house_nums}


with open(input_file, encoding="utf-8") as i_file:
    pile = [parse_cards(line) for line in i_file]
    prize = 0
    for card in pile:
        points = 0.5 if any(
            [True for x in card['house'] if x in card['client']]
          ) else 0
        for num in card['house']:
            points *= 2 if num in card['client'] else 1
        prize += points
    print(int(prize))
    i_file.close()
