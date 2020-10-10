def dotProduct(A, B, C, D):
    ab, cd = [0, 0], [0, 0]
    ab[0] = B[0]-A[0]
    ab[1] = B[1]-A[1]
    cd[0] = D[0]-C[0]
    cd[1] = D[1]-C[1]

    return ab[0]*cd[0] + ab[1]*cd[1]

print(dotProduct([0, 0], [4, 0], [4, 0], [6, 4]))
