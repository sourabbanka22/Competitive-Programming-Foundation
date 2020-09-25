def minRewards(scores):
    # Write your code here.
    rewards = [1 for score in scores]
    localMins = {}
    localMaxs = {}
    if len(scores) == 1:
        return sum(rewards)
    
    if scores[0]<scores[1]:
        localMins[0] = True
    elif scores[0]>scores[1]:
        localMaxs[0] = True
    
    for index in range(1, len(scores)-1):
        if scores[index]<scores[index-1] and scores[index]<scores[index+1]:
            localMins[index] = True
        elif scores[index]>scores[index-1] and scores[index]>scores[index+1]:
            localMaxs[index] = True
    
    if scores[len(scores)-2]>scores[-1]:
        localMins[len(scores)-1] = True
    elif scores[len(scores)-2]<scores[-1]:
        localMaxs[len(scores)-1] = True
    
    for minimum in localMins:
        left = minimum-1
        right = minimum+1
        while left>=0 and left not in localMaxs:
            rewards[left] += rewards[left+1]
            left -= 1
        
        while right<len(scores) and right not in localMaxs:
            rewards[right] += rewards[right-1]
            right += 1
        
    for maximum in localMaxs:
        leftMax = 0
        rightMax = 0
        
        if maximum-1>=0:
            leftMax = rewards[maximum-1]
        if maximum+1<len(scores):
            rightMax = rewards[maximum+1]
        rewards[maximum] = max(leftMax, rightMax)+1
    
    return sum(rewards)
    
print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))