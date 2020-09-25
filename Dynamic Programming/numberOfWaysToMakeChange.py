def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [0 for _ in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for index in range(1, n+1):
            if index>=denom:
                ways[index] += ways[index-denom]

    return ways[n]

print(numberOfWaysToMakeChange(25, [1, 5, 10, 25]))