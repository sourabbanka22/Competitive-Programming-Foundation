def minRewards(scores):
    # Write your code here.
    rewards = [1 for score in scores]

    for leftIdx in range(1, len(scores)):
        if scores[leftIdx]>scores[leftIdx-1]:
            rewards[leftIdx] = rewards[leftIdx-1]+1

    for rightIdx in reversed(range(len(scores)-1)):
        if scores[rightIdx]>scores[rightIdx+1]:
            rewards[rightIdx] = max(rewards[rightIdx], rewards[rightIdx+1]+1)
    
    return sum(rewards)

print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))