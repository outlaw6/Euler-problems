# Prime factorization
def isPrime(x):
    ''' This function checks if a number is a prime
    '''
    c=2
    
    if x == 1:
        return True
    if x == 2:
        return True
      
    while c < x:
        if x % c != 0:
            c += 1
        else:
            return False
            break
    return True

container = []

for x in range(1,200):
    if isPrime(x):    container.append(x)

factors = []
num = 13195
x=1
while x < range(len(container)):

    while num % container[x] == 0:
        num /= container[x]
        print container[x], "<---- factors"
        
    x += 1
    if num == 1:
        print "Finit0, it was a little bit tricky I admit"
        break
