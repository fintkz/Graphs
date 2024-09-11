# Eulerian Path Graph

This project implements an algo that can determine whether a graph contains an Eulerian path or not.

## Features

- Create an undirected graph
- Check if the graph is connected
- Determine the number of unbalanced nodes the graph has
- Find an Eulerian path if it exists

## Usage

1. Create a Graph object
2. Add edges to the graph using `add_edge(node1, node2)`
3. Use `has_eulerian_path()` to check for an Eulerian path
4. If an Eulerian path exists, use `find_eulerian_path()` to get the path

## Example

```python
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')

eulerian_type = g.has_eulerian_path()
if eulerian_type:
    print(f"Graph contains an {eulerian_type}")
    if eulerian_type == 'Eulerian Path':
        print("Eulerian Path:", g.find_eulerian_path())
else:
    print("Graph doesn't contain an Eulerian Path or Circuit")
```

## Definitions

- An unbalanced node is a node with an odd number of edges connected to it.
- For a connected graph to have an Eulerian path, it needs to have exactly 2 unbalanced nodes, if any.
