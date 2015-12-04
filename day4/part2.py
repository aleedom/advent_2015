import hashlib


def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


def get_answer(string):
    count = 0
    while True:
        test = string+str(count)
        res = computeMD5hash(test)
        t = res[:6]
        if t == '000000':
            break
        count += 1
    return count

print(get_answer('bgvyzdsv'))
