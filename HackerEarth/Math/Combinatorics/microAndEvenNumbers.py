def pascalTriangle(lastRow):
    matrix = [[0 for _ in range(lastRow)] for _ in range(lastRow)]
    for idx in range(lastRow):
        matrix[0][idx], matrix[idx][0] = 1, 1
    
    for row in range(1, lastRow):
        for col in range(1, lastRow):
            matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
    
    return matrix

N, K = map(int, input().split())
integers = list(map(int, input().split()))
evenCount = 0

for val in integers:
    if val%2 == 0:
        evenCount += 1

triangle = pascalTriangle(evenCount)

if evenCount == K:
    print(1)
elif evenCount < K:
    print(0)
else:
    print(triangle[K][evenCount-K])