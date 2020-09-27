def longestIncreasingSubsequence(array):
    # Write your code here.
    sequences = [None for _ in array]
    indices = [None for _ in range(len(array)+1)]
    length = 0
    for index, value in enumerate(array):
        newLength = binarySearch(1, length, indices, array, value)
        sequences[index] = indices[newLength-1]
        indices[newLength] = index
        length = max(length, newLength)
        # print(sequences)
        # print(indices)
        # print("")
    return buildSequence(array,sequences, indices[length])    

def binarySearch(startIdx, endIdx, indices, array, num):
    if startIdx>endIdx:
        return startIdx
    midIdx = (startIdx+endIdx)//2
    if array[indices[midIdx]]<num:
        startIdx = midIdx+1
    else:
        endIdx = midIdx-1
    return binarySearch(startIdx, endIdx, indices, array, num)

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))

print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))