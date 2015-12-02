def get_area(l, w, h):
    return 2*l*w+2*w*h+2*h*l + min(l*w, w*h, h*l)


def test():
    assert(get_area(2, 3, 4) == 58)
    assert(get_area(1, 1, 10) == 43)


def get_answer():
    with open('input.txt', 'r') as infile:
        total_area = 0
        for line in infile:
            l, w, h = [int(x) for x in line.split('x')]
            total_area += get_area(l, w, h)
    return total_area


test()
print(get_answer())
