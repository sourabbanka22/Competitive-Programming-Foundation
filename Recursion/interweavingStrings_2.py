def interweavingStrings(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
        return False
    
    memo = [[None for col in range(len(two)+1)] for row in range(len(one)+1)]
    result = interweavingStringsUtil(0, 0, one, two, three, memo)
    for row in memo:
        print(row)
    return result

def interweavingStringsUtil(idxOne, idxTwo, one, two, three, memo):
    if memo[idxOne][idxTwo]:
        return True
    
    idxThree = idxOne + idxTwo
    if idxThree == len(three):
        return True
    #print("One: "+ one[:idxOne+1] + " Two: "+ two[:idxTwo+1])
    if idxOne<len(one) and one[idxOne] == three[idxThree]:
        memo[idxOne+1][idxTwo] = interweavingStringsUtil(idxOne+1, idxTwo, one, two, three, memo)
        if memo[idxOne+1][idxTwo]:
            return True
    
    if idxTwo<len(two) and two[idxTwo] == three[idxThree]:
        memo[idxOne][idxTwo+1] = interweavingStringsUtil(idxOne, idxTwo+1, one, two, three, memo)
        return memo[idxOne][idxTwo+1]
    
    memo[idxOne][idxTwo] = False
    return False

# print(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"))

# print(interweavingStrings("aabcc", "dbbca", "aadbbcbcac"))

#print(interweavingStrings("aaa", "aaab", "aaabaaa"))

print(interweavingStrings("aaab", "aaaaa", "aaaaaaaab"))