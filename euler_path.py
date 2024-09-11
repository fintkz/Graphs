from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_edge(self, node1, node2):
        self.graph[node1].remove(node2)
        self.graph[node2].remove(node1)

    def depth_first_search(self, start_node, visited):
        visited[start_node] = True
        for adjacent_node in self.graph[start_node]:
            if not visited[adjacent_node]:
                self.depth_first_search(adjacent_node, visited)

    def is_connected(self):
        visited = {node: False for node in self.graph}
        # Find a node with at least one edge
        start_node = next((node for node in self.graph if self.graph[node]), None)
        # If no node with edges is found, the graph is connected
        if start_node is None:
            return True
        # Start DFS traversal from a node with at least one edge
        self.depth_first_search(start_node, visited)
        # Check if all nodes with edges are visited
        return all(visited[node] or not self.graph[node] for node in self.graph)

    def has_eulerian_path(self):
        if not self.is_connected():
            return False
        # Count unbalanced nodes (nodes with an odd number of edges)
        unbalanced_node_count = sum(1 for node in self.graph if len(self.graph[node]) % 2 != 0)
        if unbalanced_node_count == 0:
            return 'No unbalanced nodes'
        elif unbalanced_node_count == 2:
            return 'Exactly 2 unbalanced nodes'
        else:
            return False

    def find_eulerian_path(self):
        eulerian_path = []
        start_node = next(iter(self.graph))
        current_node = start_node
        while self.graph[current_node]:
            next_node = self.graph[current_node][0]
            if len(self.graph[current_node]) == 1:
                # If the current node has only one adjacent node
                eulerian_path.append((current_node, next_node))
                self.remove_edge(current_node, next_node)
            else:
                # If there are multiple adjacent nodes
                for node in self.graph[current_node]:
                    if not self.is_bridge(current_node, node):
                        next_node = node
                        break
                eulerian_path.append((current_node, next_node))
                self.remove_edge(current_node, next_node)
            current_node = next_node
        return eulerian_path

    def is_bridge(self, node1, node2):
        # Remove edge (node1, node2) and check if the graph becomes disconnected
        self.remove_edge(node1, node2)
        visited = {node: False for node in self.graph}
        self.depth_first_search(node1, visited)
        # Add edge (node1, node2) back
        self.add_edge(node1, node2)
        return not visited[node2]

# Graph 1 
g1 = Graph()
g1.add_edge('A', 'B')
g1.add_edge('A', 'C')
g1.add_edge('A', 'D')
g1.add_edge('B', 'C')
g1.add_edge('C', 'D')

# Graph 2 
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('A', 'D')
g2.add_edge('B', 'C')
g2.add_edge('B', 'E')
g2.add_edge('C', 'D')
g2.add_edge('D', 'E')
g2.add_edge('B', 'D')

# Graph 3 
g3 = Graph()
g3.add_edge('A', 'B')
g3.add_edge('A', 'C')
g3.add_edge('A', 'D')
g3.add_edge('B', 'C')
g3.add_edge('B', 'D')
g3.add_edge('C', 'D')

for g in [g1, g2, g3]:    
    eulerian_type = g.has_eulerian_path()
    if eulerian_type:
        print(f"Graph contains {eulerian_type}")
        if eulerian_type == 'Exactly 2 unbalanced nodes':
            print("Eulerian Path:", g.find_eulerian_path())
        elif eulerian_type == 'No unbalanced nodes':
            print("Eulerian Path:", g.find_eulerian_path())
    else:
        print("Graph does not have a valid Eulerian path")
