# Numpy

import numpy as np
import copy

class Graph():
    def __init__(self):
        self.adj = []
        # self.vertexToIndex = {}
        self.vertexToIndex = [] # index of the col, corresponds to index of col / row in matrix
        
    def addVertex(self, data):
        if len(self.adj) == 0:
            self.adj = np.zeros((1,1))
            # self.vertexToIndex[data] = 0
            self.vertexToIndex.append(data)

        else:
            col = np.zeros((np.shape(self.adj)[1],1))
            # add column
            self.adj = np.hstack((self.adj,col))
            # add row
            row = np.zeros((1,np.shape(self.adj)[1]))
            self.adj = np.append(self.adj, row, axis=0)
            # self.vertexToIndex[data] = len(self.adj) - 1
            self.vertexToIndex.append(data)
            
    def removeVertex(self, data):
        # Remove the vertex data from the graph.
        # Assume the value of data is unique within the graph.  
        vertex = self.vertexToIndex.index(data)
        self.adj = np.delete(self.adj, vertex,0)
        self.adj = np.delete(self.adj, np.s_[vertex],1)
        # for key, value in self.vertexToIndex.item():
        del self.vertexToIndex[self.vertexToIndex.index(data)]
        # need to decrement everything that comes after data by 1
        
    def addEdge(self, src, dest, weight = 1):
        srcIndex = self.vertexToIndex.index(src)
        destIndex = self.vertexToIndex.index(dest)
        self.adj[srcIndex][destIndex] = weight
        
    def addUndirectedEdge(self, A, B, weight = 1):
        # Adds an undirected edge with weight between the vertex A and the vertex B       
        A_index = self.vertexToIndex.index(A)
        B_index = self.vertexToIndex.index(B)
        self.adj[A_index][B_index] = weight
        self.adj[B_index][A_index] = weight
        
    def removeEdge(self,src,dest):
        srcIndex = self.vertexToIndex.index(src)
        destIndex = self.vertexToIndex.index(dest)
        self.adj[srcIndex][destIndex] = 0
        
    def removeUndirectedEdge(self, A, B, weight = 1):
        self.removeEdge(A,B)
        self.removeEdge(B,A)
        
    def V(self):
        # Return a list of all vertices.
        return self.vertexToIndex
    
    def E(self):
        # Return a list of all edges, defined as a list of 3-tuples (src, dest, weight). def neighbors(self, data: Any) -> list:
        edges=[]
        for i in self.vertexToIndex: # iterate through index of vertices
            src = self.vertexToIndex[self.vertexToIndex.index(i)]
            row = self.adj[self.vertexToIndex.index(i)]
            for j, k in enumerate(row):
                dest = self.vertexToIndex[j]
                if k != 0:
                    edges.append([src,dest, int(k)])
        return edges
    
    def neighbors(self,value):
        # Returns a list of values of the neighbors of the vertex data in the graph.
        # We consider a vertex B a neighbor of vertex A if and only if the vertex A points to B.
        neighbors = []
        for i, j in enumerate(self.adj[self.vertexToIndex.index(value)]): # iterate down column where value is 
            if j != 0: # get nonzero edges
                neighbors.append(self.vertexToIndex[i]) # add neighbor
        return neighbors
    
    def dft(self, src):
        ret = [] # where we store visited vertex by BFT
        stack = [] # initialize queue
        stack.append(src) # initialize initial list 
        visited = [src] # enqueue source into queue
        while len(stack) != 0: # if queue is empty: STOP
            vertex = stack.pop(len(stack)-1) # dequeue vertex from queue
            ret.append(vertex) # mark as seen by adding to ret
            for neighbor in sorted(self.neighbors(vertex), reverse=True): # look at neighbors of vertex (sorted b/c)
                if neighbor in stack:
                    del stack[stack.index(neighbor)]
                    stack.append(neighbor)
                if neighbor not in visited and neighbor not in stack: # if neighbor hasn't been seen, add to queue and to visited
                    stack.append(neighbor) 
                    visited.append(vertex)
        return ret
    
    def bft(self, src):
        # make a queue (FIFO)
        # start with first vertex
        # check neighbors (all the non-empty cols)
        # Perform breadth-first traversal starting from the vertex with the value src
        # Return a list of the values of the vertices you visited in order.    
        queue = []
        visited = []
        x = self.neighbors(src)
        for i in x:
            queue.append(i)
        visited.append(src)

        while len(queue) != 0:
            vertex = queue.pop(0)
            visited.append(vertex)
            w = self.neighbors(vertex)
            for i in w:
                if i not in visited and i not in queue:
                    queue.append(i)
        return visited
    
    def isDirected(self):
        if np.array_equal(self.adj, self.adj.T):
            return False
        else:
            return True
            
    def isCyclic(self):
        # path that contains the same vertex for its initial and final vertex
        # need to check if the cycle that's formed just going back
        # check if it is Directed : can return True (Undirected, need to check )
        # traverse using dft / bft starting from every vertex (b/c might be unconnected)
        
        # Checks whether the graph has a cycle.
        # Since each edge would connect the two vertices in both directions for an undirected
        # graph, such a graph is cyclic if a cyclic path exists beyond these two vertices.
       
        # 1. find a path (DFT or BFT, but keep track of entire path)
        # 2. check if it it's directed: if yes: return True
            # if vertex in path: 
            # if isUndirected() and path[-1] != path[-3]: returne True
               
        # remove edge with no incoming edges (and all its outgoing edges)
        # repeat
        # if there's a cycle, there'll be something left, if there's nothing left: no cycle
        
        def inDegree0(graph, node):
            # tells us if the node has a degree 0 (no incoming edges)
            for edgeList in graph.adj:
                for dest in edgeList:
                    if node == dest:
                        return False
            return True

        if self.isDirected():
            newGraph = Graph()
            newGraph.adj = copy.deepcopy(self.adj)
            
            for node in newGraph.V():
                print(inDegree0(newGraph, node),node)
            while len(newGraph.V()) != 0:
                n = None
                for node in newGraph.V():
                    if inDegree0(newGraph, node):
                        n = node
                        break  
                if n == None:
                    return True 
                newGraph.removeVertex(n)
            return False
        
        else:
            stack = []
            visited = []
            parent = {}

            src = self.V()[0]
            stack.append(src)
            visited.append(src)
            parent[src] = None

            while len(stack) != 0:
                v = stack.pop()
                neighbors = self.neighbors(v)    
                if parent[v] != None:
                    neighbors.remove(parent[v])
                for n in neighbors:
                    if n not in visited:
                        visited.append(n)
                        stack.append(n)
                        parent[n] = v

                    else:
                        return True
                print(stack)
            return False
    def isConnected(self):
        # Checks whether the graph is (weakly) connected
        for vertex in self.vertexToIndex:
            if not self.adj[vertex].any(): # check if rows are empty
                if not self.adj[:,vertex].any(): # check if cols are empty
                    return False
        return True
            
    def isTree(self):
        return self.isConnected() and not self.isCyclic()
    def __repr__(self): 
        # print(repr(self.adj))
        return f"{self.adj}\nIndex: {self.vertexToIndex}"
    def get_index(self):
        return self.vertexToIndex
    def get_adj(self):
        return self.adj