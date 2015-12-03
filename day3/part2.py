def update_cords(x, y, char, num_visited):
    if char == '>':
        x += 1
    elif char == '<':
        x -= 1
    elif char == '^':
        y += 1
    else:  # no down arrow on my keyboard :(
        y -= 1
    num_visited.add('{},{}'.format(x, y))
    return x, y

with open('input.txt', 'r') as infile:
    x1, x2, y1, y2 = 0, 0, 0, 0

    num_visited = {'0,0'}
    index = 1
    for char in infile.readline():
        if index % 2 == 0:
            x1, y1 = update_cords(x1, y1, char, num_visited)
        else:
            x2, y2 = update_cords(x2, y2, char, num_visited)
        index += 1
        print(len(num_visited))
