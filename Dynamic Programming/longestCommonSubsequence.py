def longestCommonSubsequence(str1, str2):
    # Write your code here.
    colLength = len(str1)+1
    rowLength = len(str2)+1
    memo = [[0 for _ in range(colLength)] for _ in range(rowLength)]

    for row in range(1, rowLength):
        for col in range(1, colLength):
            if str2[row-1] == str1[col-1]:
                memo[row][col] = memo[row-1][col-1]+1
            else:
                memo[row][col] = max(memo[row-1][col], memo[row][col-1])

    commonSeq = []
    col = colLength-1
    row = rowLength-1
    while col>0 and row>0:
        left = memo[row][col] == memo[row][col-1]
        top = memo[row][col] == memo[row-1][col]
        if left:
            col -= 1
        elif top:
            row -= 1
        else:
            commonSeq.append(str1[col-1])
            row-=1
            col-=1

    return commonSeq[::-1]

print(longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))