def knapsackProblem(items, capacity):
    memo = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
    for row in range(1, len(items)+1):
        for col in range(capacity+1):
            currentWeight = items[row-1][1]
            currentValue = items[row-1][0]
            if currentWeight<=col:
                memo[row][col] = max(memo[row-1][col-currentWeight]+currentValue, memo[row-1][col])
            else:
                memo[row][col] = memo[row-1][col]
        
    itemIndices = []
    row = len(items)
    col = capacity
    while col>0 and row>0:
        top = memo[row][col] == memo[row-1][col]
        if not top:
            itemIndices.append(row-1)
            col -= items[row-1][1]
        row-=1

    return [memo[-1][-1], itemIndices[::-1]]

print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))