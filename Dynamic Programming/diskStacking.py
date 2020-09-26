def diskStacking(disks):
    # Write your code here.
    disks.sort(key=lambda x:x[2])
    maxHeight = [disk[2] for disk in disks]
    diskTrackers = [None for _ in disks]

    for index in range(1, len(disks)):
        maxSum = float("-inf")
        prevIdx = None
        for leftIdx in range(index):
            width = disks[index][0]>disks[leftIdx][0]
            depth = disks[index][1]>disks[leftIdx][1]
            height = disks[index][2]>disks[leftIdx][2]
            currentSum = maxHeight[index]+maxHeight[leftIdx]
            if width and depth and height and currentSum>maxSum:
                maxSum = currentSum
                prevIdx = leftIdx

        maxHeight[index] = maxSum if maxSum != float("-inf") else maxHeight[index]
        diskTrackers[index] = prevIdx
    
    maxIdx = maxHeight.index(max(maxHeight))
    stackedDiscs = [disks[maxIdx]]
    while diskTrackers[maxIdx] is not None:
        stackedDiscs.append(disks[diskTrackers[maxIdx]])
        maxIdx = diskTrackers[maxIdx]
    
    return stackedDiscs[::-1]

print(diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]))
