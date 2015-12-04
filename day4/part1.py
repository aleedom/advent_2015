import hashlib


def test():
    assert(get_answer('abcdef') == 609043)
    assert(get_answer('pqrstuv') == 1048970)
    print("tests passed!")


def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


def get_answer(string):
    count = 0
    while True:
        test = string+str(count)
        res = computeMD5hash(test)
        t = res[:5]
        if t == '00000':
            break
        count += 1
    return count

test()
print(get_answer('bgvyzdsv'))
