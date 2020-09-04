def riverSizes(matrix):
    # Write your code here.
    auxillary = [[False for col in matrix[0]] for row in matrix]
	result = []
	
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if not auxillary[row][col] and matrix[row][col]:
				result.append(getSize(row, col, matrix, auxillary))
	return result

def getSize(row, col, matrix, auxillary):
	if auxillary[row][col] or matrix[row][col] == 0:
		return 0
	
	auxillary[row][col] = True
	
	toBeVisited = []
	if row+1 < len(matrix):
		toBeVisited.append([row+1, col])
	if col+1 < len(matrix[0]):
		toBeVisited.append([row, col+1])
	if row-1 >= 0:
		toBeVisited.append([row-1, col])
	if col-1 >= 0:
		toBeVisited.append([row, col-1])
	
	if len(toBeVisited) == 0:
		return 1
	elif len(toBeVisited) == 1:
		return 1 + getSize(toBeVisited[0][0], toBeVisited[0][1], matrix, auxillary)
	elif len(toBeVisited) == 2:
		return 1 + getSize(toBeVisited[0][0], toBeVisited[0][1], matrix, auxillary) + getSize(toBeVisited[1][0], toBeVisited[1][1], matrix, auxillary)
	elif len(toBeVisited) == 3:
		return 1 + getSize(toBeVisited[0][0], toBeVisited[0][1], matrix, auxillary) + getSize(toBeVisited[1][0], toBeVisited[1][1], matrix, auxillary) + getSize(toBeVisited[2][0], toBeVisited[2][1], matrix, auxillary)
	elif len(toBeVisited) == 4:
		return 1 + getSize(toBeVisited[0][0], toBeVisited[0][1], matrix, auxillary) + getSize(toBeVisited[1][0], toBeVisited[1][1], matrix, auxillary) + getSize(toBeVisited[2][0], toBeVisited[2][1], matrix, auxillary) + getSize(toBeVisited[3][0], toBeVisited[3][1], matrix, auxillary)

	

print("Start")
print(riverSizes([[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]))
print("End")