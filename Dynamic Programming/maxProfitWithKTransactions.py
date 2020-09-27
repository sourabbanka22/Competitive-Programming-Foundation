def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    memo = [[0 for _ in prices] for _ in range(2)]
    result = 0
    for row in range(1, k+1):
        maxThusFar = float("-inf")
        for col in range(1, len(prices)):
            maxThusFar = max(maxThusFar, memo[0][col-1]-prices[col-1])
            memo[1][col] = max(memo[1][col-1], maxThusFar+prices[col])
        memo[0] = memo[1]
        result = memo[1][-1]
        memo[1] = [0 for _ in prices]
    
    
    return result if len(prices) else 0

print(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2))