def underscorifySubstring(string, substring):
    # Write your code here.
    positions = getPositions(string, substring)
    underscorifiedList = []
    newPositions = []
    
    for position in positions:
        newPositions.append(position[0])
        newPositions.append(position[1])
    
    currentIdx = 0
    for index in range(len(string)):
        if currentIdx<len(newPositions) and index == newPositions[currentIdx]:
            underscorifiedList.append("_")
            currentIdx += 1
        underscorifiedList.append(string[index])
    if len(newPositions) != 0 and newPositions[-1] == len(string):
        underscorifiedList.append("_")
    
    return "".join(underscorifiedList)

def getPositions(string, substring):
    unCollapsed = []
    for index in range(len(string)):
        position = string.find(substring, index, index+len(substring))
        if position != -1:
            unCollapsed.append([position, position+len(substring)])
    
    return collapse(unCollapsed)

def collapse(unCollapsed):
    collapsed = []
    index = 0
    
    while index<len(unCollapsed)-1:
        collapsed.append([unCollapsed[index][0]])
        while index<len(unCollapsed)-1 and unCollapsed[index][1] >= unCollapsed[index+1][0]:
            index += 1
        collapsed[-1].append(unCollapsed[index][1])
        index += 1
    
    if len(unCollapsed) == 1:
        return unCollapsed
    elif len(collapsed) != 0 and collapsed[-1][1] != unCollapsed[-1][1]:
        collapsed.append(unCollapsed[-1])

    return collapsed

print(underscorifySubstring("abcabcabcabcabcabcabcabcabcabcabcabcabcabc", "abc"))        
