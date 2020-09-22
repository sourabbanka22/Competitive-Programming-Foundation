def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    bigStringReversed = bigString[::-1]
    notReversedStr = getString(bigString, smallString)
    reverseStr = getString(bigStringReversed, smallString)
    if len(notReversedStr)<len(reverseStr):
        return notReversedStr
    else:
        return reverseStr[::-1]

def getString(bigString, smallString):
    smallStringMapper = getMappedString(smallString)
    bigStringMapper = getMappedString(bigString)

    if noSmallestSubstring(smallStringMapper, bigStringMapper):
        return ""

    finalLeftPointer = 0
    finalRightPointer = len(bigString)

    currentMapper = {}
    for char in smallStringMapper:
        currentMapper[char] = 0
    
    leftPointer = 0
    rightPointer = getInitialRightPointer(bigString, currentMapper, smallStringMapper)
    
    while rightPointer<len(bigString):
        while isSubString(smallStringMapper, currentMapper):
            if finalRightPointer-finalLeftPointer > rightPointer-leftPointer:
                finalLeftPointer, finalRightPointer = leftPointer, rightPointer
            if bigString[leftPointer] in currentMapper:
                currentMapper[bigString[leftPointer]] -= 1
            leftPointer += 1
        
        if bigString[leftPointer] in currentMapper:
            currentMapper[bigString[leftPointer]] -= 1
        leftPointer += 1

        if bigString[rightPointer] in currentMapper:
            currentMapper[bigString[rightPointer]] += 1
        rightPointer += 1

    return bigString[finalLeftPointer:finalRightPointer]

def getMappedString(string):
    stringMapper = {}
    for char in string:
        if char not in stringMapper:
            stringMapper[char] = 1
        else:
            stringMapper[char] += 1
    return stringMapper

def noSmallestSubstring(smallStringMapper, bigStringMapper):
    for key in smallStringMapper:
        if key not in bigStringMapper or smallStringMapper[key]>bigStringMapper[key]:
            return True
    return False

def isSubString(smallStringMapper, currentMapper):
    for key in smallStringMapper:
        if smallStringMapper[key] > currentMapper[key]:
            return False
    return True

def getInitialRightPointer(bigString, currentMapper, smallStringMapper):
    rightPointer = 0
    
    while rightPointer<len(bigString):
        if bigString[rightPointer] in currentMapper:
            currentMapper[bigString[rightPointer]] += 1
        rightPointer += 1
        if isSubString(smallStringMapper, currentMapper):
            break
    
    return rightPointer

print(smallestSubstringContaining("abzacdwejxjfxztghiwjtklmnopqrstuvwxyz", "aajjttwwxxzz")) # "abzacdwejxjfxztghiwjt"
print(smallestSubstringContaining("a$fuu+afff+affaffa+a$Affab+a+a+$a$", "a+$aaAaaaa$++")) # "affa+a$Affab+a+a+$a"
print(smallestSubstringContaining("1456243561288281932363365412356789901!", "123!")) # "2356789901!"
print(smallestSubstringContaining("14562435612!88281932363365$412356789901", "#!123!")) # ""