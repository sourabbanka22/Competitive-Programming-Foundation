def groupAnagrams(words):
    # Write your code here.
    memo = words[:]
    for index in range(len(words)):
        words[index] = "".join(sorted(words[index]))
    
    resultMapper = {}
    for index in range(len(words)):
        if words[index] in resultMapper:
            resultMapper[words[index]].append(memo[index])
        else:
            resultMapper[words[index]] = [memo[index]]

    return list(resultMapper.values())

print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))