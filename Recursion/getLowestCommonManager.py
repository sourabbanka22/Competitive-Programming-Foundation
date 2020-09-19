def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    return getLowestCommonManagerUtil(topManager, reportOne, reportTwo).lcm

def getLowestCommonManagerUtil(manager, reportOne, reportTwo):
    count = 0
    for report in manager.directReports:
        result = getLowestCommonManagerUtil(report, reportOne, reportTwo)
        # print(result.lcm, result.count)
        if result.lcm is not None:
            return result
        count += result.count
    if manager == reportOne or manager == reportTwo:
        count += 1
    lcm = manager if count == 2 else None
    return ResultLCM(lcm, count)

class ResultLCM:
    def __init__(self, lcm, count):
        self.lcm = lcm
        self.count = count

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


nodeE = OrgChart("E")
nodeF = OrgChart("F")
nodeG = OrgChart("G")
nodeH = OrgChart("H")
nodeI = OrgChart("I")
nodeD = OrgChart("D")
nodeD.directReports = [nodeH, nodeI]
nodeC = OrgChart("C")
nodeC.directReports = [nodeF, nodeG]
nodeB = OrgChart("B")
nodeB.directReports = [nodeD, nodeE]
nodeA = OrgChart("A")
nodeA.directReports = [nodeB, nodeC]

print(getLowestCommonManager(nodeA, nodeE, nodeI))


    #             A
    #           /   \
    #         B       C
    #       /   \    /  \
    #      D     E  F    G
    #     / \
    #    H    I