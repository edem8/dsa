# Traversing grapshs
# BFS - Breadth first Search
# goes wide - visit a vertice and then it's neighbors
# useful when the solution youre looking for is closer to your root vertice
#Usecase - finding shortest path in a graph, web crawling




# implementing BFS in our graph class
class Graph:
    def __init__(self):
        self.nodes = {}  # id → set of neighbor ids

    def add_edge(self, from_id, to_id):
        # Initialize sets if not present
        # And add two undirected edges
        self.nodes.setdefault(from_id, set()).add(to_id)
        self.nodes.setdefault(to_id, set()).add(from_id)  # undirected graph


    def breath_first_search(self, starting_vertice):
        # keep track of visited and neighbouring vertices to explore 
        visited = []
        to_explore = []
        to_explore.append(starting_vertice)

        # while we have vertices to explore we want to keep visting their neighbours
        while len(to_explore) > 0:
            next = to_explore[0]
            del to_explore[0]

            visited.append(next)
            neighbors  = sorted(self.nodes[next]) 
            # This return a sorted list of neighbours 

            for neighbor in neighbors:
                if neighbor  not in visited or neighbor not  in to_explore:
                    to_explore.append(neighbor)
        return visited


    def __repr__(self):
        return "\n".join(f"{node}: {neighs}" for node, neighs in self.nodes.items())


