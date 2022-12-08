from graph import Graph

def dijkstras(graph, src):
    pass

def runDijkstras():
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
    output = []
    for i in g.vertexToIndex:
        output.append(dijkstras(g,i))
    return output