from graph import Graph

def prim(graph):
    
    def sort_tuple(tup):
        tup.sort(key = lambda x: x[2])
        return tup
    
       
    mst = []
    mstSet = []
    vertices = graph.V()
    neighbors = []
    for i in graph.neighbors(vertices[0]):
        neighbors.append(i)
    mstSet.append(vertices[0])        
    edges = sort_tuple(graph.E()) # sort edges by weight
    minumum_edge = float('inf')
    # while set(mstSet) != set(vertices):
    for m in range(len(vertices)):
        for j in edges: # (src,dest,weight)
            if j[0] in mstSet and j[1] in neighbors and j[1] not in mstSet:
                mst.append(j) # add (src,dest,weight) to mst
                mstSet.append(j[1]) # add vertex to list of vertices that have been visited          
                neighbors.remove(j[1]) # remove vertex from list of vertices that need to be checked
                minumum_edge = j[2] # set new min. to be the newly added edge weight
                break
            for k in graph.neighbors(j[1]): # add neighbors of new vertex into list of vertices to be checked
                if k not in neighbors and k not in mstSet:
                    neighbors.append(k)
            
    print(mst, 'mst')
    print(mstSet, 'mstSet')

    return mst


def runPrim():
    # loading dataset
    import json
    with open('data.json','r') as f:
        data = json.load(f)
    g = Graph()
    for k in data.keys():
        g.addVertex(k)

    # add weight of distance btw 2 cities
    for k, v in data.items():
        for k0, v0 in data.items():
            if k != k0: # means you're looking at 2 diff cities
                weight = ((v[0]-v0[0])**2 + (v[1]-v0[1])**2)**0.5  
                g.addEdge(k, k0, weight) # should be an edge btw the cities
                
    return prim(g)