from math import*
x = 0
i = 1 
for i in range(4, 8):
    uf = sqrt((15 / pow(4, (1-x))) + pow(4, (x - 1)))
    if uf == 32:
        print(x)
    x += i

print("Javob:", x)



