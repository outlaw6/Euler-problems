def fib(n):

    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


container = []

for x in range(1,31):
    container.append(fib(x))

print container # we print the first 30 fibonaccis, I dont have enough CPU power to go to 4mils...

container2 = []

for x in container: 
    if x % 2 == 0: # we check for the even ones, even though this could be done up in one step
        container2.append(x)

print sum(container2) # we sum the first 30 fibonaccis

