
a = 1
b = 1
c = 1

for x in range(2,50):
    for c in range(2,50):
        for z in range(2,50):
            if x*x + c*c + z*z == 1000:
                if x < c < z:
                    print x,c,z
