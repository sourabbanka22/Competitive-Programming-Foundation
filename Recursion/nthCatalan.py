def nthCatalan(n):
    # Write your code here.
    memo = [1]

    for right in range(1, n+1):
        nth = 0
        for left in range(right):
            i = memo[left]
            j = memo[right-1-left]
            nth += i*j
        memo.append(nth)
        
    return memo[n]

print(nthCatalan(5))