def multiKeySort(array):
    array.sort(key = lambda x: [x[0], x[1]])
    return array

array = [[0, 5], [5, 1], [2, 3], [4, 2], [-1, 3], [0, 15], [0, 1], [8, 3]]
print(multiKeySort(array))