import os
import math


day_08_input = "/inputs/08_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_08_input)


def parse_instructions(left_right):
    return [0 if x == 'L' else 1 for x in left_right]


def node_map(raw_node_list):
    node_refs = [(x).split(' ') for x in raw_node_list]
    node_table = [{x[0]: (x[2][1:4], x[3][:3])} for x in node_refs]
    table = {}
    [table.update(x) for x in node_table]
    return table


def step_count(node_map, instructions, start='AAA'):
    limit = len(instructions)
    end = ''
    point = start
    steps = 0
    while end != 'Z':
        ref = steps % limit if steps >= limit else steps
        check = node_map.get(point)[instructions[ref]]
        end = check[2]
        point = check
        steps += 1
    return steps


with open(input_file, encoding="utf-8") as i_file:
    raw = i_file.readlines()
    cleaned = list(filter(lambda x: x != '',
                          [line.strip() for line in raw]))
    instructions = cleaned[0]
    raw_nodes = cleaned[1:]
    table = node_map(raw_nodes)
    parsed_coord = parse_instructions(instructions)
    a_end = list(filter(lambda x: x[2] == 'A', table.keys()))
    steps = [step_count(table, parsed_coord, x) for x in a_end]
    all_z_end = math.lcm(*steps)
    print(all_z_end)
    i_file.close()
