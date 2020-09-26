def levenshteinDistance(str1, str2):
    # Write your code here.
    colLength = len(str1)+1
    rowLength = len(str2)+1
    result = 0
    
    memo = [[None for _ in range(colLength)] for _ in range(2)]
    for col in range(colLength):
        memo[0][col] = col

    for row in range(1, rowLength):
        memo[1][0] = row
        for col in range(1, colLength):
            if str2[row-1] == str1[col-1]:
                memo[1][col] = memo[0][col-1]
            else:
                memo[1][col] = min(memo[0][col], memo[0][col-1], memo[1][col-1]) + 1
        result = memo[1][colLength-1]
        memo[0] = memo[1]
        memo[1] = [None for col in range(colLength)]

    return result


print(levenshteinDistance("abc", "yabd"))