# Kruskal's Algorithm Algorithm

```python
```python
# Kruskal's Algorithm

## 1. Category / Type
"""
Kruskal's Algorithm falls under the category of Minimum Spanning Tree (MST) algorithms. It is a greedy algorithm designed to find the minimum spanning tree for a connected, undirected graph with weighted edges.
"""

## 2. Core Idea / Intuition
"""
The core idea of Kruskal's Algorithm is to sort all the edges of the graph in non-decreasing order of their weights and then add them one by one to the growing spanning tree. The key is to ensure that adding an edge does not form a cycle. This is achieved by using a Union-Find data structure to detect cycles.
"""

## 3. Steps / Flow
"""
1. **Sort all the edges**: Begin by sorting all edges in the graph by their weight in non-decreasing order.
2. **Initialize subsets**: Create a subset for each vertex with only that vertex in it. Initially, each vertex is its own parent, and the rank is 0.
3. **Iterate through the sorted edges**: For each edge, do the following:
   - Check if the edge can be added without forming a cycle using the Union-Find structure.
   - If it can be added (i.e., the two vertices of the edge are in different subsets), include the edge in the result and union the two subsets.
4. **Stop when the spanning tree has V-1 edges**: Since a minimum spanning tree for a graph with V vertices has exactly V-1 edges, stop the process when you have V-1 edges in the tree.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space  |
|---------|---------|---------|--------|
| O(E log E) | O(E log V) | O(E log V) | O(V + E) |

- Here, E is the number of edges, and V is the number of vertices.
- The complexity is dominated by the sorting step, and the Union-Find operations are nearly constant time (amortized).
"""

## 5. Use Cases
"""
- Network Design: Building network designs like LAN, WAN, etc., where the cost must be minimized.
- Approximation algorithms: Used as a subroutine in other algorithms like clustering to approximate solutions.
- Circuit design: Minimizing the length of wire needed to connect components in a circuit.
"""

## 6. Common Variants
"""
- Prim's Algorithm: Another popular algorithm for finding the minimum spanning tree, which grows the MST one vertex at a time.
- Borůvka's Algorithm: A lesser-known but effective algorithm that works by adding the cheapest edge from each component.
"""

## 7. Trade-offs
"""
- Kruskal's Algorithm is more efficient on graphs with many edges (dense graphs) due to its sorting step.
- It is not suitable for graphs that are represented using adjacency matrices due to higher space complexity.
- Compared to Prim's, Kruskal's is simpler to implement using edge list and is advantageous for graphs with more edges.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure that the graph is connected; otherwise, a spanning tree cannot be formed.
- Properly implement and optimize the Union-Find data structure to avoid incorrect cycle detection.
"""

## 9. Classic Problems
"""
- Constructing the minimum cost spanning tree in a graph.
- Finding safe and efficient routes in transportation and logistics networks.
"""

## 10. Code Implementation (Demo)
def kruskal_mst(graph):
    # A class to represent a graph edge
    class Edge:
        def __init__(self, u, v, weight):
            self.u = u
            self.v = v
            self.weight = weight

    # A class to represent a subset for union-find
    class Subset:
        def __init__(self, parent, rank):
            self.parent = parent
            self.rank = rank

    # A utility function to find the set of an element i (uses path compression technique)
    def find(subsets, i):
        if subsets[i].parent != i:
            subsets[i].parent = find(subsets, subsets[i].parent)
        return subsets[i].parent

    # A function that does union of two sets of x and y (uses union by rank)
    def union(subsets, x, y):
        xroot = find(subsets, x)
        yroot = find(subsets, y)

        if subsets[xroot].rank < subsets[yroot].rank:
            subsets[xroot].parent = yroot
        elif subsets[xroot].rank > subsets[yroot].rank:
            subsets[yroot].parent = xroot
        else:
            subsets[yroot].parent = xroot
            subsets[xroot].rank += 1

    # The main function to construct MST using Kruskal's algorithm
    result = []  # This will store the resultant MST
    i, e = 0, 0  # i - sorted edges index, e - result index

    # Step 1: Sort all the edges in non-decreasing order of their weight
    graph = sorted(graph, key=lambda item: item[2])

    subsets = [Subset(v, 0) for v in range(len(graph))]

    while e < len(graph) - 1:
        u, v, w = graph[i]
        i += 1
        x = find(subsets, u)
        y = find(subsets, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(subsets, x, y)

    return result

# Example usage:
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst = kruskal_mst(edges)
for u, v, weight in mst:
    print(f"Edge: {u}-{v} Weight: {weight}")
```
```