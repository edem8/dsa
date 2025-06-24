# Graphs have like nodes and edges which establishes some realtion between nodes
# so like some node is connected to another node


class Node:
    def __init__(self, id):
        self.id = id
        # nodes are connected to other nodes - list of nodes
        self.neighbours = []


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, id_1, id_2):
        node1 = node2 = None

        # Find nodes by their IDs
        for node in self.nodes:
            if node.id == id_1:
                node1 = node
            elif node.id == id_2:
                node2 = node

        if node1 and node2:
            node1.neighbours.append(node2)
            node2.neighbours.append(node1)


#  In a real world application like a social application you have more dense relations and
#  And so you probably want to store data as a matrix - a list of lists
"""
    A  B  C  
A [ 0  1  0 ]
B [ 1  0  1 ]
C [ 0  1  0 ]


0 and 1s are boolean values that represent whether or not there exist a relationship between associated nodes

"""


class SocialGraph:
    def __init__(self, num_nodes):
        # Since people start of without having friends the relations should be false - 0
        self.nodes = []
        for i in range(num_nodes):
            new_list = []
            for j in range(num_nodes):
                # fill up the new list with false relationships
                new_list[j] = False
            self.nodes.append(new_list)

    def add_edge(self, i, j):
        # i and j and the row and colum to add the edge(relationship) to True
        if i == j:
            return
        if i < 0 and j < 0:
            return
        if i >= len(self.nodes) and j >= len(self.nodes):
            return

        self.node[i][j] = True
        # For non directional graphs then
        self.node[j][i] = True
