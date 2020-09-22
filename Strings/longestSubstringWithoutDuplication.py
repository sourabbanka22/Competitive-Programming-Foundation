def longestSubstringWithoutDuplication(string):
    # Write your code here.
    finalLeft, finalRight = 0, 0
    for index in range(len(string)):
        considered = {}
        left, right = index, index
        while left>=0 and right<len(string):
            if finalRight-finalLeft < right-left:
                finalLeft, finalRight = left, right

            if string[left] not in considered:
                considered[string[left]] = True
                left -= 1
            if string[right] not in considered:
                considered[string[right]] = True
                right += 1
            
            if string[left] in considered and string[right] in considered:
                break
    
    return string[finalLeft:finalRight+1]

print(longestSubstringWithoutDuplication("clementisacap"))