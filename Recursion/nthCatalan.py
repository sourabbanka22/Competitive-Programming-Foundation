def nthCatalan(n):
    # Write your code here.
    memo = [None for val in range(n+1)]
    memo[0] = 1
    return nthCatalanUtil(n, memo)

def nthCatalanUtil(n, memo):
    if memo[n] is not None:
        # print("Cheers to Memorization")
        return memo[n]
    
    numOfTrees = 0
    for left in range(n):
        right = n-1-left
        numOfLeftTrees = nthCatalanUtil(left)
        numOfRightTrees = nthCatalanUtil(right)
        numOfTrees += numOfLeftTrees*numOfRightTrees
    memo[n] = numOfTrees
    return numOfTrees

print(nthCatalan(4))