# Prim's Algorithm

## 1. Category / Type
"""
Prim's Algorithm falls under the category of Graph Algorithms. It is specifically used for finding the Minimum Spanning Tree (MST) of a weighted, undirected graph.
"""

## 2. Core Idea / Intuition
"""
The core idea of Prim's Algorithm is to grow the Minimum Spanning Tree (MST) one vertex at a time, starting from an arbitrary vertex and expanding by adding the smallest edge that connects the growing MST to a vertex that is not yet in the MST. This ensures that the MST remains connected and grows optimally with each step.
"""

## 3. Steps / Flow
"""
1. Initialize a set to keep track of vertices included in the MST (initially empty).
2. Choose an arbitrary vertex to start the MST.
3. Initialize a priority queue (or a min-heap) to keep track of edges connecting the MST to vertices outside it, sorted by weight.
4. While the number of edges in the MST is less than (V-1), repeat the following:
   - Extract the edge with the minimum weight from the priority queue.
   - If the edge connects a vertex in the MST to a vertex outside it, add this edge to the MST.
   - Add the new vertex to the MST set.
   - For the newly added vertex, add all edges connecting it to vertices outside the MST to the priority queue.
5. Continue until the MST includes all vertices.
"""

## 4. Time & Space Complexity
"""
| Best     | Average | Worst   | Space  |
|----------|---------|---------|--------|
| O(E log V) | O(E log V) | O(E log V) | O(V^2) |

- E is the number of edges, and V is the number of vertices in the graph.
- The time complexity is dominated by the priority queue operations.
"""

## 5. Use Cases
"""
Prim's Algorithm is used in network design, such as designing the least costly network of cables or pipes, and in any scenario where a minimum spanning structure is needed, such as in clustering algorithms.
"""

## 6. Common Variants
"""
- Kruskal's Algorithm: Another algorithm to find the MST, but it sorts all edges first and adds them one by one.
- Reverse-delete Algorithm: Starts with all edges and removes the largest edges one by one without disconnecting the graph.
"""

## 7. Trade-offs
"""
- Prim's Algorithm is more efficient on dense graphs compared to Kruskal's since it uses adjacency matrices or lists.
- On sparse graphs, Kruskal's can be more efficient due to sorting edges upfront.
- Requires a priority queue for optimal performance, which can add implementation complexity.
"""

## 8. Pitfalls / Gotchas
"""
- Choosing the right data structures (e.g., priority queue) is crucial for maintaining efficiency.
- Ensuring that the graph is connected; otherwise, the algorithm cannot produce a single spanning tree.
- Handling graphs with multiple components requires running the algorithm independently on each component.
"""

## 9. Classic Problems
"""
- Network design problems (e.g., road networks, electrical grids).
- Cluster analysis using MST-based methods.
- Approximate solutions to the Traveling Salesman Problem (TSP).
"""

## 10. Code Implementation (Demo)
def prims_algorithm(graph, start_vertex):
    import heapq
    from collections import defaultdict

    mst_edges = []
    visited = set()
    min_heap = [(0, start_vertex, None)]  # (weight, vertex, parent)

    while min_heap and len(visited) < len(graph):
        weight, current_vertex, parent = heapq.heappop(min_heap)
        
        if current_vertex not in visited:
            visited.add(current_vertex)
            if parent is not None:
                mst_edges.append((parent, current_vertex, weight))
            
            for neighbor, edge_weight in graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))

    return mst_edges

# Example usage:
# graph = {
#     'A': [('B', 1), ('C', 3)],
#     'B': [('A', 1), ('C', 2), ('D', 4)],
#     'C': [('A', 3), ('B', 2), ('D', 5)],
#     'D': [('B', 4), ('C', 5)]
# }
# start_vertex = 'A'
# print(prims_algorithm(graph, start_vertex))
