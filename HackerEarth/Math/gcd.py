def getGCD(a, b):
    while b:
        a, b = b, a%b
    return a


print(getGCD(12, 44))