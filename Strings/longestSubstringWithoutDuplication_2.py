def longestSubstringWithoutDuplication(string):
    # Write your code here.
    final = [0, 0]
    considered = {}
    currentLeft = 0
    for index in range(len(string)):
        current = string[index]
        if current in considered:
            currentLeft = max(currentLeft, considered[current]+1)
        if final[1]-final[0] < index+1-currentLeft:
            final[0], final[1] = currentLeft, index+1
        
        considered[current] = index

    return string[final[0]:final[1]]

print(longestSubstringWithoutDuplication("clementisacap"))