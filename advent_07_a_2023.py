import os
import pprint


day_07_input = "/inputs/07_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_07_input)


def count_labels(hand, labels):
    count_labels = [len(list(filter(lambda y: y == x, hand))) for x in labels]
    return count_labels


def map_values(hand):
    VALUES = {
     'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9,
     '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3,
     '3': 2, '2': 1,
     }

    mapped = [VALUES.get(x) for x in hand]
    return mapped


def classify_cards(hand, bet):
    unique_labels = set(*hand.split())
    label_count = count_labels(hand, unique_labels)
    if len(label_count) == 1:
        return (map_values(list(*hand.split())),
                hand, bet, 7)
    if len(label_count) == 2:
        return (map_values(list(*hand.split())),
                hand, bet, 6) if 4 in label_count else (
            map_values(list(*hand.split())), hand, bet, 5)
    if len(label_count) == 3:
        return (map_values(list(*hand.split())),
                hand, bet, 4) if 3 in label_count else (
            map_values(list(*hand.split())), hand, bet, 3)
    if len(label_count) == 4:
        return (map_values(list(*hand.split())),
                hand, bet, 2)
    if len(label_count) == 5:
        return (map_values(list(*hand.split())), hand, bet, 1)


with open(input_file, encoding="utf-8") as i_file:
    raw = i_file.readlines()
    hands = [hand.strip().split(' ') for hand in raw]
    classified_hands = [classify_cards(hand[0], int(hand[1]))
                        for hand in hands]
    ranked_hands = sorted(classified_hands,
                          key=lambda x: (
                            x[3],
                            x[0][0],
                            x[0][1],
                            x[0][2],
                            x[0][3],
                            x[0][4],
                                        )
                          )
    total_winnings = ([x[2] * (ind + 1) for ind, x
                       in enumerate(ranked_hands)])
    pprint.pprint(sum(total_winnings))
    i_file.close()
