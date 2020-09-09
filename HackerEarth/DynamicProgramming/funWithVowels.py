def funWithVowels(stringInput):
    mapper = {
        "a": 1,
        "e": 2,
        "i": 3,
        "o": 4,
        "u": 5,
    }

    temp = []
    s = []

    length = len(stringInput)
    count = 0

    for i in range(length):
        value = mapper.get(stringInput[i], -1)

        if value == -1:
            continue
        else:
            s.append(stringInput[i])
            count += 1
            temp.append(value)
    print(s)
    print(temp)
    memo = [0]*count
    for i in range(count):
        memo[i] = 1 if temp[i]==1 else 0
    print(memo)
    for i in range(count):
        j = 0
        while j<i:
            if (temp[j]==temp[i]-1 or temp[j]==temp[i]) and memo[j] >= mapper.get(s[j]):
                memo[i] = max(memo[i], memo[j]+1)
            j+=1
    print(memo)
    result = 0
    for i in range(count):
        if s[i] == "u":
            result = max(result, memo[i])
    
    return result

stringInput = "aaaeeeeegjbodnodfnboidnbooofksdvipsfvifbondfbonfklkvssifuu"
result = funWithVowels(stringInput)

print(result)