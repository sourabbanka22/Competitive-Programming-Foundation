def pascalTriangle(lastRow):
    matrix = [[0 for _ in range(lastRow)] for _ in range(lastRow)]
    for idx in range(lastRow):
        matrix[0][idx], matrix[idx][0] = 1, 1
    
    for row in range(1, lastRow):
        for col in range(1, lastRow):
            matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]

    return matrix


print(pascalTriangle(5))