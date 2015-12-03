with open('input.txt', 'r') as infile:
    curr_x = 0
    curr_y = 0
    num_visited = {'0,0'}
    for char in infile.readline():
        if char == '>':
            curr_x += 1
        elif char == '<':
            curr_x -= 1
        elif char == '^':
            curr_y += 1
        else:
            curr_y -= 1
        num_visited.add('{},{}'.format(curr_x, curr_y))
        print(len(num_visited))
