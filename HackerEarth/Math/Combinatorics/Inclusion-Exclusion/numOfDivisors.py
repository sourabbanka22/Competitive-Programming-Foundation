def getGCD(a, b):
    while b:
        a, b = b, a%b
    return a

def countSetBits(x):
    return bin(x).count('1') 

def inclusionExclusion(primes, n): 

    odd = 0
    even = 0
    powSetSize = 1 << len(primes)

    for counter in range(1, powSetSize): 
        product = 1
        
        for idx in range(len(primes)):
            if counter & (1 << idx):
                product *= primes[idx]
        
        if countSetBits(counter) & 1:
            odd += n//product
        else:
            even += n//product
    
    return odd-even 

primes = [2, 3, 11, 13]
n = int(input())
numOfDivisors = inclusionExclusion(primes, n)

denom = getGCD(numOfDivisors, n)
print(numOfDivisors//denom, n//denom)