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


print(modularMultiplicativeInverse(5, 12))
