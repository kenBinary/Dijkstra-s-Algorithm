import networkx as network
import matplotlib.pyplot as plt


myConnections = network.Graph()


def createGraph(firstNode, secondNode, pWeight, graph):
    graph.add_edge(firstNode, secondNode, weight=pWeight)


def setSourceNode(sourceNode):
    sourceNodeNeighbors = list(myConnections.adj[sourceNode])
    graphNodes = dict(myConnections.nodes)
    graphNodes.pop(sourceNode)
    for node in graphNodes:
        if (node in sourceNodeNeighbors):
            graphNodes[node] = sourceNode
    return graphNodes


def getGraphCosts(graphNodes):
    graphWeights = {}
    for node in graphNodes:
        infinity = float("inf")
        graphWeights[node] = infinity
    return graphWeights


def getUserInput(graph):
    addMoreConnection = True
    while (addMoreConnection):
        firstNode = input("Enter the first node:")
        secondNode = input("Enter the second node:")
        edgeWeight = input("Enter the weight of the edge:")
        addConnection = input("Enter more connection? ('yes'/'no'):")
        addMoreConnection = True if addConnection == "yes" else False
        createGraph(firstNode,secondNode,edgeWeight,graph)



# getUserInput(myConnections);


createGraph("book", "record", 5, myConnections)
createGraph("book", "poster", 0, myConnections)
createGraph("record", "drum", 20, myConnections)
createGraph("record", "guitar", 15, myConnections)
createGraph("poster", "drum", 35, myConnections)
createGraph("poster", "guitar", 30, myConnections)
createGraph("guitar", "piano", 20, myConnections)
createGraph("drum", "piano", 10, myConnections)


# FINDING THE LOWEST COST NODE


# print(list(myConnections.edges))
# graphWeightsss = dict(myConnections.edges)
# print(graphWeightsss)
# for edges in list(myConnections.edges):
# print(graphWeightsss[edges]['weight'])
# currentNode = 'poster'
# print(list(myConnections.adj[currentNode]))


sourceNode = 'drum'
sourceNodeNeighbor = list(myConnections.adj[sourceNode])
visitedNodes = []


def initializeGraphCosts(graphCosts):
    for edges in graphWeights:
        for neighbor in sourceNodeNeighbor:
            if (sourceNode in edges and neighbor in edges):
                for node in graphCosts:
                    if (node == neighbor):
                        if (graphWeights[edges]['weight'] < graphCosts[node]):
                            graphCosts[node] = graphWeights[edges]['weight']
                            graphNodes[node] = sourceNode
                            # currentNode = findLowestCostNode(graphCosts)
    visitedNodes.append(sourceNode)
    return graphCosts


graphWeights = dict(myConnections.edges)
graphNodes = setSourceNode(sourceNode)
graphCosts = initializeGraphCosts(getGraphCosts(graphNodes))
# graphCosts = getGraphCosts(graphNodes)


def findLowestCostNode(graphCosts):
    lowestCost = float('inf')
    lowestCostNode = None
    for node in graphCosts:
        cost = graphCosts[node]
        if (cost < lowestCost and node not in visitedNodes):
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode


currentNode = findLowestCostNode(graphCosts)
currentNodeNeighbors = list(myConnections.adj[currentNode])
# print(currentNode)
# print(currentNodeNeighbors)


def getNeighborWeight(currentNode, neighbor):
    for edge in graphWeights:
        if (currentNode in edge and neighbor in edge):
            return graphWeights[edge]['weight']


# print(getNeighborWeight(currentNode,'poster'))
# print(graphCosts)
while currentNode is not None:
    cost = graphCosts[currentNode]  # 0
    # Go through all the neighbors of this node.
    currentNodeNeighbors = list(
        myConnections.adj[currentNode])  # record,poster
    # neighbors = graph[node]
    for neighbor in currentNodeNeighbors:
        if neighbor not in visitedNodes:
            new_cost = cost + getNeighborWeight(currentNode, neighbor)
            # If it's cheaper to get to this neighbor by going through this node...
            if new_cost < graphCosts[neighbor]:
                # ... update the cost for this node.
                graphCosts[neighbor] = new_cost
                # This node becomes the new parent for this neighbor.
                # parents[n] = node
                graphNodes[neighbor] = currentNode
    # Mark the node as processed.
    visitedNodes.append(currentNode)
    # Find the next node to process, and loop.
    currentNode = findLowestCostNode(graphCosts)

print(graphCosts)
print(graphNodes)
xx = {'book': 25,
      'record': 20,
      'poster': 25,
      'guitar': 30,
      'piano': 10}

yy = {'book': 'record',
      'record': 'drum',
      'poster': 'book',
      'guitar': 'piano',
      'piano': 'drum'}

# for edges in graphWeights:
#     for neighbor in currentNodeNeighbor:
#         if(currentNode in edges and neighbor in edges):
#             for node in graphCosts:
#                 if(node == neighbor):
#                     if(graphWeights[edges]['weight'] < graphCosts[node]):
#                         graphCosts[node] = graphWeights[edges]['weight']
#                         graphNodes[node] = currentNode
#                         visitedNodes.append(currentNode)
#                         # currentNode = findLowestCostNode(graphCosts)


# print(visitedNodes)
# print(graphNodes)
# print(graphCosts)
# print(visitedNodes)


# for node in graphCosts:
#     print(node)
# print(graphCosts)


# print(graphCosts)
# print(graphWeights)
# print(graphNodes)


# myGraph = network.to_dict_of_dicts(myConnections)


# print(myConnections.edges)
# graphEdges = list(myConnections.edges)
# graphNodes = setSourceNode('poster');

# print(graphNodes)
# for keys in graphWeights:
# print(graphWeights[keys]['weight'])

# def getGraphWeights(graphNodes):
#     graphWeights = {}
#     for node in graphNodes:
#         infinity = float("inf")
#         graphWeights[node] = infinity
# graphWeights = {}
# for node in graphNodes:
#     infinity = float("inf")
#     graphWeights[node] = infinity
# print(graphWeights)
# sourceNode = 'poster'
# sourceNodeNeighbors = list(myConnections.adj[sourceNode])
# graphNodes = dict(myConnections.nodes)
# graphNodes.pop(sourceNode)
# for node in graphNodes:
#     if (node in sourceNodeNeighbors):
#         graphNodes[node] = sourceNode
# print(graphNodes)
# test = {'book': 'poster',
#         'record': {},
#         'drum': 'poster',
#         'guitar': 'poster',
#         'piano': {}}
# plt.subplot(2, 2, 4)
# network.draw_networkx(myConnections,**options)
# network.draw_spectral(myConnections, with_labels=True)


# Draw Graph
pos = network.spring_layout(myConnections, scale=100)
network.draw(myConnections, pos, font_size=8, with_labels=True)
plt.show()
