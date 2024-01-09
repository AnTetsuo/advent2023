import os


def connection_map(cell, neighbor, direction=''):
    if neighbor == '.':
        return False

    DIR_MAP = {
        'up': 'down',
        'down': 'up',
        'left': 'right',
        'right': 'left',
    }

    CONNECTIONS = {
        'S': ['up', 'down', 'left', 'right'],
        '|': ['up', 'down'],
        'L': ['up', 'right'],
        'J': ['up', 'left'],
        '-': ['left', 'right'],
        'F': ['down', 'right'],
        '7': ['down', 'left'],
    }
    neighbor_connection = direction in CONNECTIONS.get(neighbor)
    cell_connection = DIR_MAP.get(direction) in CONNECTIONS.get(cell)

    return neighbor_connection and cell_connection


def traverse_pipes(start, grid):
    row, col = start
    above = row - 1 if row > 0 else None
    below = row + 1 if row + 1 < len(grid) else None
    prev = col - 1 if col > 0 else None
    foward = col + 1 if col + 1 < len(grid[0]) else None
    cell = grid[row][col]
    directions = ['down', 'up', 'left', 'right']
    coords = [[above, col], [below, col], [row, foward], [row, prev]]
    next_cells = [
        grid[above][col] if above is not None else '.',
        grid[below][col] if below is not None else '.',
        grid[row][foward] if foward is not None else '.',
        grid[row][prev] if prev is not None else '.',
    ]
    north, south, east, west = next_cells
    cardinals = [connection_map(cell, x, directions[ind])
                 for ind, x in enumerate(next_cells)]
    step = cardinals.index(True) if True in cardinals else False
    grid[row][col] = '.'
    return coords[step] if step is not False else step


day_10_input = "/inputs/10_input.txt"
input_path = os.getcwd()
input_file = input_path + str(day_10_input)

with open(input_file, encoding="utf-8") as i_file:
    raw_pipes = i_file.readlines()
    pipes = [list(x.strip()) for x in raw_pipes]
    hist = []
    start_row = [ind for ind, sym in enumerate(pipes) if 'S' in sym][0]
    start_col = pipes[start_row].index('S')
    hist.append([start_row, start_col])
    step = traverse_pipes([start_row, start_col], pipes)
    hist.append(step)
    while step:
        next_step = traverse_pipes(step, pipes)
        if next_step is not False:
            hist.append(next_step)
        step = next_step
    print(len(hist) / 2)
    i_file.close()
