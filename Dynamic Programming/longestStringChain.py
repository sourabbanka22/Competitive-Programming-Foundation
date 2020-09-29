def longestStringChain(strings):
    # Write your code here.
    strings.sort(key=len, reverse=True)
    stringMapper = {}
    print(strings)
    for index, string in enumerate(strings):
        stringMapper[string] = index
    
    lengthOfStrings = [[] for _ in strings]
    for index, string in enumerate(strings):
        length=len(string)
        for innerIdx in range(length):
            potentialString = string[0:innerIdx] + string[innerIdx+1:length+1]
            if potentialString in stringMapper:
                lengthOfStrings[index].append(stringMapper[potentialString])
    
    longestChainFromEachIndices =  getLongestStringChain(strings, lengthOfStrings)
    longestChain = []
    for chain in longestChainFromEachIndices:
        if len(chain)>len(longestChain):
            longestChain = chain
    return [strings[idx] for idx in longestChain] if len(longestChain)>1 else []

def getLongestStringChain(strings, lengthOfStrings):
    tracer = [[idx] for idx in range(len(strings))]
    print(tracer, lengthOfStrings)
    for index in reversed(range(len(strings)-1)):
        currentLongest = tracer[index]
        maximum = 0
        for val in lengthOfStrings[index]:
            if len(tracer[val])>maximum:
                currentLongest = tracer[index]+tracer[val]
                maximum = len(tracer[val])
        tracer[index] = currentLongest
    return tracer


print(longestStringChain(["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]))