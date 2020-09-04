from collections import defaultdict

class Graph: 

    def __init__(self,vertices): 
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.reachable = defaultdict(list)

    def addEdge(self,u,v): 
        self.graph[u].append(v)

    def calculateAllReachables(self):
        for vertex in self.vertices:
            self.reachable[vertex] = self.dfs(vertex)

    def dfs(self, v):
        array = []
        visited = {}
        for node in self.vertices:
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

def airportConnections(airports, routes, startingAirport):
    # Write your code here.
    Graph = createGraph(airports, routes)

    visited = {}
    for airport in airports:
        visited[airport] = False

    count = getRequiredCount(Graph, visited, startingAirport)

    return count

def getRequiredCount(Graph, visited, startingAirport):

    reachable = sorted(Graph.reachable.items(), key=lambda x: len(x[1]), reverse=True)
    count = 0
    for airport in Graph.reachable[startingAirport]:
        visited[airport] = True
    for airport in reachable:
        if not visited[airport[0]]:
            count += 1
            for connected in airport[1]:
                visited[connected] = True
    return count

def createGraph(airports, routes):

    g = Graph(airports)
    for route in routes:
        g.addEdge(route[0], route[1])
    g.calculateAllReachables()
    
    return g

print(airportConnections([
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
],[
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
],"LGA"))