def sieveOfEratosthenes(number):
    isPrime = [True for _ in range(number+1)]
    isPrime[0], isPrime[1] = False, False

    idx = 2
    while idx*idx <= number:
        multiple = 2
        currentVal = idx
        while isPrime[idx] and currentVal*multiple<=number:
            isPrime[currentVal*multiple] = False
            multiple += 1
        idx += 1
    
    count = 0
    for val in isPrime:
        if val:
            count += 1

    return count

number = int(input())
print(sieveOfEratosthenes(number))