

def testNum(x):

    for y in range(1,21):
        if x % y != 0:
            return False

    return True


for x in range(10000000, 100000000):
    if testNum(x):
        print x, testNum(x)
        break
    print x, testNum(x)
