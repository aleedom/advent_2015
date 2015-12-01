with open("input.txt", 'r') as infile:
    floor = 0
    index = 0
    for c in infile.readline():
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        index += 1
        if floor == -1:
            break
    print(index)
