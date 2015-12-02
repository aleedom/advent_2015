def get_ribbon(l, w, h):
    bow = l*w*h
    min1, min2, min3 = sorted([l, w, h])
    strap = 2*min1 + 2*min2
    return bow + strap


def test():
    assert(get_ribbon(1, 1, 10) == 14)
    assert(get_ribbon(2, 3, 4) == 34)


def get_answer():
    with open('input.txt', 'r') as infile:
        total_ribbon = 0
        for line in infile:
            l, w, h = [int(x) for x in line.split('x')]
            total_ribbon += get_ribbon(l, w, h)
    return total_ribbon


test()
print(get_answer())
