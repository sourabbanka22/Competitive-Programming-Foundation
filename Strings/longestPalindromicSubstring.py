def longestPalindromicSubstring(string):
    # Write your code here.
    maxLeft = 0
    maxRight = 1
    for index in range(len(string)-1):
        odd = getLongestPalindromicSubstring(index-1, index+1, string)
        even = getLongestPalindromicSubstring(index, index+1, string)
        currentLeftMax, currentRightMax =  odd if odd[1]-odd[0]>even[1]-even[0] else even
        if maxRight-maxLeft < currentRightMax-currentLeftMax:
            maxLeft, maxRight = currentLeftMax, currentRightMax

    return string[maxLeft: maxRight]


def getLongestPalindromicSubstring(left, right, string):
    while left>=0 and right<len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return [left+1, right]

print(longestPalindromicSubstring("abaxyzzyxf"))
print(longestPalindromicSubstring("a"))