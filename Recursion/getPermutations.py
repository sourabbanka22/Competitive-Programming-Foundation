def getPermutations(array):
    # Write your code here.
    permutations = []
    getPermutationsUtil(0, array, permutations)
    return permutations

def getPermutationsUtil(index, array, permutations):
    if index == len(array)-1:
        permutations.append(array[:])
    else:
        for idx in range(index, len(array)):
            array[idx], array[index] = array[index], array[idx]
            getPermutationsUtil(index+1, array, permutations)
            array[idx], array[index] = array[index], array[idx]

print(getPermutations([1,2,3]))