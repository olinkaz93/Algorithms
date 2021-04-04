class Graph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

        """ adjacent_list = {
        'node' : [ connected_node, another_connected node ] 
        'node2' : [ node, node, node ...]
        }
        """
        # adjacent_list:
        # {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 4], 3: [1, 4], 4: [2, 3, 5], 5: [4, 6], 6: [5]}

        # adjacent_list[0] = [ 1, 2 ]

    def addNode(self, data):
        if data not in self.adjacent_list:
            #add the node to the adjacency dictionary. End create the empty list, which will store all neighbours of the node(vertex)
            self.adjacent_list[data] = []
            self.number_of_nodes += 1
        else:
            print("the Vertex, ", data, "is already in the adjacency list")

    def addEdge(self, node1, node2):
        #unidirected graphs - we add both relationship of two nodes, when we found out that is has been no inserted already
        if node2 not in self.adjacent_list[node1]:
            #under key 'node' we store the list of the neighbor's vertexes
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)
        else:
            print("the edges are already inserted!")


if __name__ == "__main__":
    """
    new_graph = Graph()
    new_graph.addNode(5)
    print(new_graph.adjacent_list)
    new_graph.addNode(0)
    new_graph.addNode(6)
    print(new_graph.adjacent_list)
    new_graph.addEdge(5, 6)
    print(new_graph.adjacent_list)
    new_graph.addNode(5)
    """

    sample_graph = Graph()
    sample_graph.addNode(0)
    sample_graph.addNode(1)
    sample_graph.addNode(2)
    sample_graph.addNode(3)
    sample_graph.addNode(4)
    sample_graph.addNode(5)
    sample_graph.addNode(6)

    sample_graph.addEdge(0, 1)
    sample_graph.addEdge(0, 2)
    print(sample_graph.adjacent_list)
    sample_graph.addEdge(0, 2)
    sample_graph.addEdge(1, 0)
    sample_graph.addEdge(1, 2)
    sample_graph.addEdge(1, 3)
    sample_graph.addEdge(2, 0)
    sample_graph.addEdge(2, 1)
    sample_graph.addEdge(2, 4)
    sample_graph.addEdge(3, 1)
    sample_graph.addEdge(3, 4)
    sample_graph.addEdge(4, 2)
    sample_graph.addEdge(4, 3)
    sample_graph.addEdge(4, 5)
    sample_graph.addEdge(5, 4)
    sample_graph.addEdge(5, 6)
    sample_graph.addEdge(6, 5)

    print(sample_graph.adjacent_list)
    print(sample_graph.adjacent_list[0])
    print(type(sample_graph.adjacent_list))




