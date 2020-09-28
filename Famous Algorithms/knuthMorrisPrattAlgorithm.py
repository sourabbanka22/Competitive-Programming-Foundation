def knuthMorrisPrattAlgorithm(string, substring):
    # Write your code here.
    pattern = buildPattern(substring)
    return containsSubstring(string, substring, pattern)

def buildPattern(substring):
    pattern = [-1 for _ in substring]
    leftIdx = 0
    index = 1
    while index<len(substring):
        if substring[leftIdx]==substring[index]:
            pattern[index] = leftIdx
            leftIdx += 1
            index += 1
        else:
            if leftIdx>0:
                leftIdx = pattern[leftIdx-1]+1
            else:
                index += 1

    return pattern

def containsSubstring(string, substring, pattern):
    stringIdx = 0
    subStringIdx = 0

    while stringIdx+len(substring)-subStringIdx <= len(string):
        if string[stringIdx] == substring[subStringIdx]:
            if subStringIdx == len(substring)-1:
                return True
            stringIdx += 1
            subStringIdx += 1
        else:
            if subStringIdx>0:
                subStringIdx = pattern[subStringIdx-1]+1
            else:
                stringIdx += 1
    return False

print(knuthMorrisPrattAlgorithm("aefoaefcdaefcdaed", "aefcdaed"))