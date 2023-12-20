import os
import pprint


day_07_input = "/inputs/07_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_07_input)


def map_values(hand):
    VALUES = {
     'A': 13, 'K': 12, 'Q': 11, 'T': 10,
     '9': 9, '8': 8, '7': 7, '6': 6,
     '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1
     }

    mapped = [VALUES.get(x) for x in hand]
    return mapped


def count_labels(hand, labels):
    count_labels = [len(list(filter(lambda y: y == x, hand))) for x in labels]
    if 'J' in hand:
        values = map_values(list(labels))
        list_with_J = [[list(labels)[ind], values[ind], x]
                       for ind, x in enumerate(count_labels)]
        no_J = list(filter(lambda x: x[0] != 'J', list_with_J))
        if not no_J:
            return count_labels
        no_J.sort(key=lambda x: (-x[2], -x[1]))
        J_index = list(labels).index('J')
        no_J[0][2] += list_with_J[J_index][2]
        return [x[2] for x in no_J]
    return count_labels


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
