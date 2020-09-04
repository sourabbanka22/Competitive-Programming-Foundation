from collections import defaultdict

class Graph: 

    def __init__(self,vertices): 
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v): 
        self.graph[u].append(v)

    def dfs(self, v):
        array = []
        visited = {}
        for node in self.V:
            visited[node] = False
        return self.dfsUtil(v, array, visited)

    def dfsUtil(self, v, array, visited):

        if visited[v] == True:
            return
        visited[v] = True
        array.append(v)

        for adj in self.graph[v]:
            self.dfsUtil(adj, array, visited)
        
        return array

    def bfs(self, v):
        visited = {}
        for node in self.V:
            visited[node] = False
        array = []
        queue = []
        queue.append(v)

        visited[v] = True

        while len(queue) != 0:
            current = queue.pop(0)
            array.append(current)
            for adj in self.graph[current]:
                if visited[adj] != True:
                    queue.append(adj)
                visited[adj] = True
        
        return array


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)
        
        return array

    def bfs(self, array):
        queue = [self]
        while len(queue)>0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        
        return array

nodes = [
  "BGI",
  "CDG",
  "DEL",
  "DOH",
  "DSM",
  "EWR",
  "EYW",
  "HND",
  "ICN",
  "JFK",
  "LGA",
  "LHR",
  "ORD",
  "SAN",
  "SFO",
  "SIN",
  "TLV",
  "BUD"
]
routes = [
  ["DSM", "ORD"],
  ["ORD", "BGI"],
  ["BGI", "LGA"],
  ["SIN", "CDG"],
  ["CDG", "SIN"],
  ["CDG", "BUD"],
  ["DEL", "DOH"],
  ["DEL", "CDG"],
  ["TLV", "DEL"],
  ["EWR", "HND"],
  ["HND", "ICN"],
  ["HND", "JFK"],
  ["ICN", "JFK"],
  ["JFK", "LGA"],
  ["EYW", "LHR"],
  ["LHR", "SFO"],
  ["SFO", "SAN"],
  ["SFO", "DSM"],
  ["SAN", "EYW"]
]


g = Graph(nodes)
for route in routes:
    g.addEdge(route[0], route[1])


print("Following is Depth First Traversal")  
print(g.dfs("DEL"))

print("Following is Breath First Traversal")  
print(g.bfs("DEL"))