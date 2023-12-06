"""First day of advent of code"""
import os


def filter_numbers(characters):
    """characters: string[]
    responsabilities:
      check which character in
      the characters list
      is a number,
      and return it
    filtering: number[]"""
    characters = list(characters)
    filtering = [char for char in characters if char.isnumeric()]

    return filtering


day_01_input = "/inputs/01_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_01_input)

with open(input_file, encoding="utf-8") as i_file:
    sum_coordinates = 0
    for line in i_file:
        coordinates = [num for num in filter_numbers(line)]
        sum_coordinates += int(coordinates[0] + coordinates[-1])
    print(sum_coordinates)
    i_file.close()
