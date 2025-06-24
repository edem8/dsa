


class Graph:
    def __init__(self):
        self.nodes = {}  # id → set of neighbor ids

    def add_edge(self, from_id, to_id):
        # Initialize sets if not present
        # And add two undirected edges
        self.nodes.setdefault(from_id, set()).add(to_id)
        self.nodes.setdefault(to_id, set()).add(from_id)  # undirected graph

    def __repr__(self):
        return "\n".join(f"{node}: {neighs}" for node, neighs in self.nodes.items())





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
