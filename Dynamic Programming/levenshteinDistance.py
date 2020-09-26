def levenshteinDistance(str1, str2):
    # Write your code here.
    colLength = len(str1)+1
    rowLength = len(str2)+1
    memo = [[None for _ in range(colLength)] for _ in range(rowLength)]
    for col in range(colLength):
        memo[0][col] = col
    for row in range(rowLength):
        memo[row][0] = row

    for row in range(1, rowLength):
        for col in range(1, colLength):
            if str2[row-1] == str1[col-1]:
                memo[row][col] = memo[row-1][col-1]
            else:
                memo[row][col] = min(memo[row-1][col], memo[row-1][col-1], memo[row][col-1]) + 1

    return memo[rowLength-1][colLength-1]


print(levenshteinDistance("abc", "yabd"))