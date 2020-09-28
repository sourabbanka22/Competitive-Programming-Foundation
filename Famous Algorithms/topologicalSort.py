def topologicalSort(jobs, deps):
    # Write your code here.
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for preReq, job in deps:
        graph.addPreReq(job, preReq)
    return graph

def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = depthFirstTraverse(node, orderedJobs)
        # containsCycle = depthFirstTraverse(node, orderedJobs, 0)
        if containsCycle:
            return []
    return orderedJobs

def depthFirstTraverse(node, orderedJobs):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for preReqNode in node.preReqs:
        # print("Node: ", node.job, "preReqNode: ", preReqNode.job)
        # containsCycle = depthFirstTraverse(preReqNode, orderedJobs, depth+1)
        containsCycle = depthFirstTraverse(preReqNode, orderedJobs)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    # print("Depth: ", depth, "Node: ", node.job)
    orderedJobs.append(node.job)
    return False

class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)
    
    def addPreReq(self, job, preReq):
        jobNode = self.getNode(job)
        preReqNode = self.getNode(preReq)
        jobNode.preReqs.append(preReqNode)
    
    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

class JobNode:
    def __init__(self, job):
        self.job = job
        self.preReqs = []
        self.visited = False
        self.visiting = False

print(topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]))
