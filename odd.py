


def main(number):
    
    counter = 0

    x1 = number % 10
    counter += x1 * 1000
    number //= 10  

    x2 = number % 10
    counter += x2 * 100
    number //= 10  

    x3 = number % 10
    counter += x3 * 10
    number //= 10  

    x4 = number % 10
    counter += x4
    number //= 10  
    
    return counter

print(main(1521))