def patternMatcher(pattern, string):
    # Write your code here.
    newPattern = getNewPattern(pattern)
    didSwitch = pattern[0] != newPattern[0]
    counts = {"x":0, "y": 0}
    firstYPosition = getFirstYPositionAndCounts(newPattern, counts)

    if counts["y"] != 0:
        for xLen in range(1, len(string)):
            yLen = (len(string) - xLen*counts["x"])/counts["y"]
            if yLen <=0 or yLen%1 != 0:
                continue
            yLen = int(yLen)
            yPos = xLen*firstYPosition
            x = string[:xLen]
            y = string[yPos:yPos+yLen]
            potentialMatch = map(lambda char: x if char=="x" else y, newPattern)
            if string == "".join(potentialMatch):
                return [y, x] if didSwitch else [x, y]
    else:
        xLen = len(string)/counts["x"]
        if xLen%1 == 0:
            xLen = int(xLen)
            x = string[:xLen]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return ["", x] if didSwitch else [x, ""]

    return []

def getNewPattern(pattern):
    newPattern = list(pattern)
    if newPattern[0] == "x":
        return newPattern
    else:
        return list(map(lambda char: "x" if char == "y" else "y", newPattern))


def getFirstYPositionAndCounts(newPattern, counts):
    firstYPosition = None
    for index, char in enumerate(newPattern):
        counts[char] += 1
        if firstYPosition is None and char == "y":
            firstYPosition = index
    return firstYPosition

print(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"))