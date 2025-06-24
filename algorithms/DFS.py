# DFS - depth First Search
# goes deep - go in and backtrack to follow a different branch doesnt need to keep track of "to visit list"
# useful when the solution youre looking for is kind of far away - say a maze.


# implementing DFS in our graph class
class Graph:
    def __init__(self):
        self.nodes = {}  # id → set of neighbor ids

    def add_edge(self, from_id, to_id):
        # Initialize sets if not present
        # And add two undirected edges
        self.nodes.setdefault(from_id, set()).add(to_id)
        self.nodes.setdefault(to_id, set()).add(from_id)  # undirected graph

    def depth_first_search(self, start_vertice, visited=None):
        # unlike bfs here we only track visited
        # basicall 1. Pick a starting vertice
        # 2. Pick on of its child node (neighbours doesnt matter which one) and dfs that too
        if visited is None:
            visited = []

        if start_vertice not in visited:
            visited.append(start_vertice)

            for neighbor in sorted(self.nodes[start_vertice]):
                self.depth_first_search(neighbor, visited)

        return visited

    def __repr__(self):
        return "\n".join(f"{node}: {neighs}" for node, neighs in self.nodes.items())
