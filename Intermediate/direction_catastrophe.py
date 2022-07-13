# In a map, there are given directions some of which cancel each other...
# N, E, E, W, S, N, W, S ===>>>  And the person is back where it started. Hence this code will simply the map, directions
# N, E, E, W, S, N, W    ===>>>  N  [The person would be standing relatively north to where it was before], and so on...

nswe = {
    "N" : 0,
    "S" : 0,
    "W" : 0,
    "E" : 0,
}

def reduceDir(dir_s):
    final_Dir = []

    for dir_ in dir_s:
        nswe[dir_.upper()[0]] += 1

    nswe['N'] -= nswe['S']
    nswe['W'] -= nswe['E']

    if nswe['N'] > 0:
        final_Dir.extend(["NORTH"] * nswe['N'])
    elif nswe['N'] < 0:
        final_Dir.extend(["SOUTH"] * -nswe['N'])

    if nswe['W'] > 0:
        final_Dir.extend(["WEST"] * nswe['W'])
    elif nswe['W'] < 0:
        final_Dir.extend(["EAST"] * -nswe['W'])

    return final_Dir


if __name__ == "__main__":
    print(reduceDir(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']))      ## WEST