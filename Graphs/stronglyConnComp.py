from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
		self.V= vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	def DFSUtil(self,v,visited): 
		visited[v]= True
		print(v)
		for i in self.graph[v]: 
			if visited[i]==False: 
				self.DFSUtil(i,visited)

	def dfs(self, v):
		array = []
		visited = [False for vertices in range(self.V)]

		return self.dfsUtil(v, array, visited)
	
	def dfsUtil(self, v, array, visited):

		if visited[v] == True:
			return
		visited[v] = True
		array.append(v)

		for adj in self.graph[v]:
			self.dfsUtil(adj, array, visited)
		
		return array

	def fillOrder(self,v,visited, stack): 
		visited[v]= True
		for i in self.graph[v]: 
			if visited[i]==False: 
				self.fillOrder(i, visited, stack) 
		stack = stack.append(v) 
	
	def getTranspose(self): 
		g = Graph(self.V) 

		for i in self.graph: 
			for j in self.graph[i]: 
				g.addEdge(j,i) 
		return g 

	def printSCCs(self): 
		
		stack = []
		visited =[False]*(self.V)

		for i in range(self.V): 
			if visited[i]==False: 
				self.fillOrder(i, visited, stack) 

		gr = self.getTranspose() 
		
		visited =[False]*(self.V) 

		while stack: 
			i = stack.pop() 
			if visited[i]==False: 
				gr.DFSUtil(i, visited) 
				print("")

g = Graph(5)
g.addEdge(1, 0)  
g.addEdge(0, 2)  
g.addEdge(2, 1)  
g.addEdge(0, 3)  
g.addEdge(1, 4)
  
print("Following is Depth First Traversal")  
print(g.dfs(0))
