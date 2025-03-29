# Dijkstra's Algorithm

## 1. Category / Type
"""
Dijkstra's Algorithm is a graph search algorithm that falls under the category of shortest path algorithms. It is designed to find the shortest path from a single source vertex to all other vertices in a graph with non-negative edge weights.
"""

## 2. Core Idea / Intuition
"""
The core idea of Dijkstra's Algorithm is to iteratively select the vertex with the smallest tentative distance from the source, update its neighbors with the shortest known paths, and repeat this process until all vertices have been processed. This method ensures that the shortest path to each vertex is found in a greedy manner, leveraging a priority queue to efficiently select the next vertex to process.
"""

## 3. Steps / Flow
"""
1. Initialize distances: Set the distance to the source vertex to 0 and all other vertices to infinity.
2. Create a priority queue (min-heap) and insert the source vertex with a distance of 0.
3. While the priority queue is not empty, do the following:
   - Extract the vertex `u` with the smallest distance from the priority queue.
   - For each neighbor `v` of `u`, calculate the tentative distance from the source to `v` through `u`.
   - If the calculated distance is less than the known distance to `v`, update the distance to `v` and insert `v` into the priority queue.
4. Repeat until all vertices have been processed and the priority queue is empty.
"""

## 4. Time & Space Complexity
"""
| Best      | Average     | Worst      | Space     |
|-----------|-------------|------------|-----------|
| O(E + V)  | O((V + E) log V) | O((V + E) log V) | O(V)      |

- E is the number of edges.
- V is the number of vertices.
- The complexity is commonly expressed as O((V + E) log V) due to the use of a priority queue (min-heap).
"""

## 5. Use Cases
"""
- Network routing protocols (e.g., OSPF, IS-IS)
- GPS navigation systems for finding the shortest route
- Solving pathfinding problems in games
- Analyzing transportation networks for optimal paths
"""

## 6. Common Variants
"""
- A* Algorithm: A variant that uses heuristics to improve performance in certain scenarios.
- Bellman-Ford Algorithm: Used when graphs have negative weight edges.
- Johnson's Algorithm: Efficient for dense graphs requiring all-pairs shortest paths.
"""

## 7. Trade-offs
"""
- Dijkstra's Algorithm is not suitable for graphs with negative edge weights as it assumes that once a vertex is processed, its shortest path is finalized.
- It is efficient for dense graphs when implemented with a Fibonacci heap, but simpler implementations with binary heaps are more practical for sparse graphs.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure all edge weights are non-negative to avoid incorrect results.
- Be cautious with graph representations; adjacency lists are typically more efficient for sparse graphs.
- Properly handle disconnected graphs, where some vertices may remain unreachable.
"""

## 9. Classic Problems
"""
- Finding the shortest path in a road network with known distances.
- Optimizing delivery routes for logistics and transportation.
- Analyzing social networks to determine closeness between individuals.
"""

## 10. Code Implementation (Demo)
def dijkstra(graph, start_vertex):
    import heapq
    # Initialize distances and priority queue
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nodes can only be visited once
        if current_distance > distances[current_vertex]:
            continue

        # Check neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
