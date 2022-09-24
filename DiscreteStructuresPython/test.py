import networkx as network
import matplotlib.pyplot as plt



testGraph = {
    0: {1,2},
    1: {0,3},
    2: {0,3},
    3 : {1,2,5,4},
    4 : {3,5,6},
    5 : {3,4,6},
    6 : {5,4},
}

myGraph = network.Graph(testGraph)
# myGraph.add_node(1)
# myGraph.add_nodes_from([2,3,4,5])
# myGraph.add_node("spam")        # adds node "spam"
# myGraph.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'

# myGraph.add_edge(1, 2)
# myGraph.add_edge(1, 3)
# myGraph.add_edge(3, 'm')


options = {
    'node_size': 300,
    'width': 3,
    'edge_color' : 'blue',
}
network.draw_networkx(myGraph)
plt.show()
