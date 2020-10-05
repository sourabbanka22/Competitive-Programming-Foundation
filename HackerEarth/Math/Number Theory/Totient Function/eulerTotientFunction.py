def getPrimeFactors(number):
    primeFactors = set()
    while number%2 == 0:
        primeFactors.add(2)
        number //= 2
    
    idx = 3
    while idx*idx <= number:
        while number%idx == 0:
            primeFactors.add(idx)
            number //= idx
        idx += 2
    
    if number>2:
        primeFactors.add(number)
    
    return primeFactors

def eulerTotientFunction(number):
    primeFactors = getPrimeFactors(number)
    
    result = number
    for val in primeFactors:
        if number%val == 0:
            result *= (1 - 1/val)
    
    return int(result)

num = int(input())
print(eulerTotientFunction(num))