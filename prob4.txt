# Problem 4 Euler

def palin(x):
    # A Python tricky way to check a palindrom
    return x == x[::-1]


def isPalindrome(x):
    # A school example of reversing string
    s = ''
    for char in x:
        s = char + s
    return s == x

container = []
for x in range(100,1000):
    for y in range(100,1000):
        for z in range(100,1000):
            s = x * y * z
            if isPalindrome(str(s)):
                container.append(str(s))


print container

