def isValidSubsequence(array, sequence):
    # Write your code here.
    childIdx = 0
    for parent in array:
        if childIdx<len(sequence) and sequence[childIdx] == parent:
            childIdx += 1

    return len(sequence) == childIdx