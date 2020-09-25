def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    coins = [float("inf") for _ in range(n+1)]
    coins[0] = 0
    for denom in denoms:
        for index in range(1, n+1):
            if index>=denom:
                coins[index] = min(coins[index], coins[index-denom]+1)

    return -1 if coins[n]==float("inf") else coins[n]

print(minNumberOfCoinsForChange(90, [1, 5, 10, 25]))