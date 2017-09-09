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
for x in range(1,190000):
    if isPrime(x):
        print x
        container.append(x)
    if len(container) > 10002:
        print "To the end!"
        print container[len(container)-1]
        break
