with open('input.txt', 'r') as infile:
    floor = 0
    for c in infile.readline():
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
    print('Last floor: {}'.format(floor))
