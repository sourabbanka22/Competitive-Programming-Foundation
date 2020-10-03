def modularExponentiation(x, n, M):
    result = 1
    
    while n>0:
        if n%2 == 1:
            result = (result*x) % M
        x = (x*x) % M
        n = n//2
    
    return result

print(modularExponentiation(5, 10, 1000))