# Floyd-Warshall Algorithm

## 1. Category / Type
"""
- Graph Algorithms
- Dynamic Programming
- Shortest Path
"""

## 2. Core Idea / Intuition
"""
The Floyd-Warshall algorithm is designed to find the shortest paths between all pairs of vertices in a weighted graph. 
The core idea is to incrementally improve the solution by considering whether a path through an intermediate vertex 
would be shorter than the direct path between two vertices. By iterating over all possible intermediate vertices, 
the algorithm refines the shortest path estimate for each pair of vertices.
"""

## 3. Steps / Flow
"""
1. Initialize a 2D array `dist[][]` of size `VxV` where `V` is the number of vertices:
   - If there is an edge from vertex `i` to `j`, then `dist[i][j]` is the weight of the edge.
   - If there is no edge from `i` to `j`, then `dist[i][j]` is set to infinity.
   - Set `dist[i][i]` to 0 for all `i`.
   
2. For each vertex `k` from `0` to `V-1`, do:
   - For each pair of vertices `(i, j)`:
     - Update `dist[i][j]` as: 
       `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
     - This step tests if a path from `i` to `j` through `k` is shorter than the current known path.
     
3. After all iterations, `dist[i][j]` will hold the shortest distance from vertex `i` to vertex `j`.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space   |
|---------|---------|---------|---------|
| O(V^3)  | O(V^3)  | O(V^3)  | O(V^2)  |

- The time complexity is O(V^3) because there are three nested loops, each running `V` times.
- The space complexity is O(V^2) due to the storage of the `dist` matrix.
"""

## 5. Use Cases
"""
- Computing shortest paths in dense graphs.
- Finding transitive closure of a graph.
- Detecting negative weight cycles (If `dist[i][i] < 0` after the algorithm execution).
"""

## 6. Common Variants
"""
- Johnson's Algorithm: A variant that reduces time complexity for sparse graphs.
- Transitive Closure: A simplified application of Floyd-Warshall that computes reachability.
"""

## 7. Trade-offs
"""
- Efficient for graphs with small to moderate vertex counts due to O(V^3) complexity.
- Not suitable for graphs with negative weight cycles as it doesn't handle them directly.
- Simplicity and ease of implementation compared to other all-pairs shortest-path algorithms.
"""

## 8. Pitfalls / Gotchas
"""
- Be cautious of integer overflow when dealing with large weights.
- Ensure that the graph does not contain negative weight cycles when interpreting the results.
- Initialize the `dist` matrix correctly, especially handling infinity for no direct paths.
"""

## 9. Classic Problems
"""
- All-pairs shortest paths in a city map with road distances.
- Network routing protocols where path optimization is required.
"""

## 10. Code Implementation (Demo)
def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf')] * V for _ in range(V)]
    
    # Initialize the solution matrix same as input graph matrix
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    
    # Adding vertices individually
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
