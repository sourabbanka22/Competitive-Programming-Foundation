def interweavingStrings(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
        return False
    
    return interweavingStringsUtil(0, 0, one, two, three)

def interweavingStringsUtil(idxOne, idxTwo, one, two, three):

    #print("One: "+ one[:idxOne+1] + " Two: "+ two[:idxTwo+1])
    idxThree = idxOne + idxTwo
    if idxThree == len(three):
        return True
    
    if idxOne<len(one) and one[idxOne] == three[idxThree]:
        if interweavingStringsUtil(idxOne+1, idxTwo, one, two, three):
            return True
    
    if idxTwo<len(two) and two[idxTwo] == three[idxThree]:
        return interweavingStringsUtil(idxOne, idxTwo+1, one, two, three)
    
    return False

# print(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"))

# print(interweavingStrings("aabcc", "dbbca", "aadbbcbcac"))

#print(interweavingStrings("aaa", "aaab", "aaabaaa"))

print(interweavingStrings("aaab", "aaaaa", "aaaaaaaab"))