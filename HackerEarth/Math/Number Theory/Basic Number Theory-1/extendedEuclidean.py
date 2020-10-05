def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0

    gcd, currentX, currentY = extendedEuclid(b, a%b)
    x = currentY
    y = currentX - (a//b)*currentY
    
    return gcd, x, y

gcd, x, y = extendedEuclid(35, 15)
print("GCD:", gcd, "  X:", x, "  Y:", y)