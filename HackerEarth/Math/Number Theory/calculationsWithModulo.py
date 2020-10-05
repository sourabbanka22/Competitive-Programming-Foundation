def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0

    gcd, currentX, currentY = extendedEuclid(b, a%b)
    x = currentY
    y = currentX - (a//b)*currentY
    
    return gcd, x, y

def modularMultiplicativeInverse(a, M):
    _, x, _ = extendedEuclid(a, M)
    return (x%M + M)%M

def modularExponentiation(x, n, M):
    result = 1
    
    while n>0:
        if n%2 == 1:
            result = (result*x) % M
        x = (x*x) % M
        n = n//2
    
    return result

a, b, c, M = map(int, input().split())
cInverse = modularMultiplicativeInverse(c, M)
first = modularExponentiation(a, b, M)
second = cInverse%M
result = (first*second)%M
print(result)
