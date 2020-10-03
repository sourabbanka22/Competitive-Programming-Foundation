def isPrime(number):
    idx = 2
    while idx*idx <= number:
        if number%idx == 0:
            return False
        idx += 1
    return True

print(isPrime(4))