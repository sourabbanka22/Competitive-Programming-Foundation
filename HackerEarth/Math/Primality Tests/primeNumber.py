import random

def modularExponentiation(x, n, M):
    result = 1
    
    while n>0:
        if n%2 == 1:
            result = (result*x) % M
        x = (x*x) % M
        n = n//2
    
    return result

def fermatTest(n, k):

    if n == 2:
        return True
    if n%2 == 0 or n < 2:
        return False

    for _ in range(k):
        a = random.randint(1, n-1)
        if modularExponentiation(a, n-1, n) != 1:
            return False
    
    return True

cases = int(input())
for case in range(cases):
    number = int(input())
    if fermatTest(number, 3):
        print("prime")
    else:
        print("composite")