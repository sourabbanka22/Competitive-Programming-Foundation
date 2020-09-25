def apartmentHunting(blocks, reqs):
    # Write your code here.
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)

def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for index in range(len(blocks)):
        if blocks[index][req]:
            closestReqIdx = index
        minDistances[index] = distanceBetween(index, closestReqIdx)
    for index in reversed(range(len(blocks))):
        if blocks[index][req]:
            closestReqIdx = index
        minDistances[index] = min(minDistances[index], distanceBetween(index, closestReqIdx))
    return minDistances

def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for index in range(len(blocks)):
        minDistancesAtBlocks = list(map(lambda distances: distances[index], minDistancesFromBlocks))
        maxDistancesAtBlocks[index] = max(minDistancesAtBlocks)
    return maxDistancesAtBlocks

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for index in range(len(array)):
        currentVal = array[index]
        if currentVal<minValue:
            minValue=currentVal
            idxAtMinValue = index
    return idxAtMinValue

def distanceBetween(a, b):
    return abs(a-b)

# blocks = [
#   {"gym": False, "school": True, "store": False},
#   {"gym": True, "school": False, "store": False},
#   {"gym": True, "school": True, "store": False},
#   {"gym": False, "school": True, "store": False},
#   {"gym": False, "school": True, "store": True}
# ]

blocks2 = [
  {"gym": True, "school": True, "store": False},
  {"gym": False, "school": False, "store": False},
  {"gym": False, "school": True, "store": False},
  {"gym": False, "school": False, "store": False},
  {"gym": False, "school": False, "store": True},
  {"gym": True, "school": False, "store": False},
  {"gym": False, "school": False, "store": False},
  {"gym": False, "school": False, "store": False},
  {"gym": False, "school": False, "store": False},
  {"gym": False, "school": True, "store": False}
]

blocks3 = [
  {"gym": True, "pool": False, "school": True, "store": False},
  {"gym": False, "pool": False, "school": False, "store": False},
  {"gym": False, "pool": False, "school": True, "store": False},
  {"gym": False, "pool": False, "school": False, "store": False},
  {"gym": False, "pool": False, "school": False, "store": True},
  {"gym": True, "pool": False, "school": False, "store": False},
  {"gym": False, "pool": False, "school": False, "store": False},
  {"gym": False, "pool": False, "school": False, "store": False},
  {"gym": False, "pool": False, "school": False, "store": False},
  {"gym": False, "pool": False, "school": True, "store": False},
  {"gym": False, "pool": True, "school": False, "store": False}
]

# reqs = ["gym", "school", "store"]
# print(apartmentHunting(blocks, reqs))
# print(apartmentHunting(blocks2, reqs))
reqs2 = ["gym", "pool", "school", "store"]
print(apartmentHunting(blocks3, reqs2))