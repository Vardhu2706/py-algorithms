# Bellman-Ford Algorithm

## 1. Category / Type
"""
The Bellman-Ford algorithm is a graph algorithm used for Single Source Shortest Path (SSSP) problems, particularly in graphs with negative weight edges.
"""

## 2. Core Idea / Intuition
"""
The core idea of the Bellman-Ford algorithm is to iteratively relax all the edges of the graph. It aims to find the shortest path from a single source to all other vertices in a weighted graph, even when some edge weights are negative. This is achieved by updating the shortest path estimates based on the edge weights, propagating improvements throughout the graph.
"""

## 3. Steps / Flow
"""
1. **Initialize distances:** Start by setting the distance to the source node to zero and all other nodes to infinity.
2. **Relax edges repeatedly:** For each edge in the graph, update the distance to the destination vertex if the path through the edge offers a shorter path.
3. **Check for negative-weight cycles:** After all edges have been relaxed V-1 times (where V is the number of vertices), perform one more iteration. If any distance can still be reduced, a negative-weight cycle exists in the graph.
"""

## 4. Time & Space Complexity
"""
| Best | Average | Worst | Space |
|------|---------|-------|-------|
| O(VE) | O(VE)  | O(VE) | O(V)  |

- V: Number of vertices
- E: Number of edges
- The algorithm's time complexity is O(VE) in all cases because it relaxes every edge V-1 times.
- The space complexity is O(V) due to the storage of distance estimates and predecessor information.
"""

## 5. Use Cases
"""
- Finding the shortest path in graphs where edges can have negative weights.
- Detecting negative weight cycles in a graph.
- Used in network routing protocols like RIP (Routing Information Protocol).
"""

## 6. Common Variants
"""
- **Johnson's Algorithm:** Uses Bellman-Ford as a subroutine to handle graphs with negative weights, allowing Dijkstra's algorithm to be used on all pairs of shortest paths.
"""

## 7. Trade-offs
"""
- **Advantages:** 
  - Handles negative weight edges.
  - Can detect negative weight cycles.
  
- **Disadvantages:** 
  - Slower compared to Dijkstra's algorithm for graphs without negative weights.
  - Not suitable for graphs with a very large number of edges due to its O(VE) complexity.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure that the graph does not contain negative weight cycles when using the algorithm for shortest path computations, as such cycles can lead to undefined behavior.
- The algorithm does not work with graphs that have self-loops with negative weights.
"""

## 9. Classic Problems
"""
- **Shortest Path with Negative Weights:** Finding the shortest path in networks where costs can be negative, such as in financial networks with credits and debits.
- **Currency Arbitrage Detection:** Finding cycles in a currency exchange graph where the product of exchange rates is greater than 1, indicating an arbitrage opportunity.
"""

## 10. Code Implementation (Demo)
def bellman_ford(graph, source):
    # Initialize distances from source to all vertices as infinite and to source itself as 0
    distance = {vertex: float('inf') for vertex in graph}
    distance[source] = 0

    # Relax edges |V|-1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distance

# Example usage:
# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('C', 3), ('D', 2), ('E', 2)],
#     'C': [],
#     'D': [('C', 5), ('B', 1)],
#     'E': [('D', -3)]
# }
# print(bellman_ford(graph, 'A'))
