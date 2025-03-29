# Topological Sort Algorithm

```python
```python
# Topological Sort Algorithm

## 1. Category / Type
"""
Topological Sort is a type of graph algorithm used for ordering the vertices of a Directed Acyclic Graph (DAG).
"""

## 2. Core Idea / Intuition
"""
The core idea behind Topological Sort is to order the vertices of a Directed Acyclic Graph (DAG) such that for every directed edge from vertex U to vertex V, U comes before V in the ordering. This is particularly useful in scenarios where certain tasks need to be completed before others, such as scheduling tasks according to prerequisites.
"""

## 3. Steps / Flow
"""
To perform a Topological Sort, follow these steps:
1. Identify a vertex with no incoming edges (i.e., in-degree of zero) and add it to the topological order.
2. Remove this vertex from the graph along with its outgoing edges.
3. Repeat steps 1 and 2 until all vertices are processed. 
4. If at any point no such vertex exists and vertices are still unprocessed, the graph is not a DAG, and a topological sorting is not possible.

The above can be implemented using Depth-First Search (DFS) or Kahn's Algorithm (indegree based).
"""

## 4. Time & Space Complexity
"""
| Best     | Average | Worst    | Space   |
|----------|---------|----------|---------|
| O(V+E)   | O(V+E)  | O(V+E)   | O(V+E)  |

Where V is the number of vertices and E is the number of edges in the graph. The complexity arises from the need to visit each vertex and edge once.
"""

## 5. Use Cases
"""
- Scheduling tasks given dependencies.
- Resolving symbol dependencies in linkers.
- Instruction scheduling in compilers.
- Determining the order of compilation tasks.
"""

## 6. Common Variants
"""
- Using Depth-First Search (DFS) to perform topological sorting.
- Using Kahn's Algorithm which involves calculating in-degrees.
"""

## 7. Trade-offs
"""
- Topological Sort only works on Directed Acyclic Graphs (DAGs).
- Requires entire graph to be known before sorting.
- Cannot be used if the graph has cycles.
"""

## 8. Pitfalls / Gotchas
"""
- Attempting to perform a topological sort on a graph with cycles will fail.
- Ensuring all vertices are part of the graph, including isolated vertices.
- Properly handling graphs with multiple starting nodes (nodes with zero in-degrees).
"""

## 9. Classic Problems
"""
- Course Schedule: Determining if all courses can be completed given prerequisites.
- Task Scheduling: Ordering tasks with dependencies.
"""

## 10. Code Implementation (Demo)
def topological_sort_kahns_algorithm(graph):
    from collections import deque

    # Step 1: Calculate in-degrees of all vertices
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    # Step 2: Collect nodes with zero in-degree
    zero_in_degree_queue = deque([u for u in graph if in_degree[u] == 0])
    
    topological_order = []
    
    # Step 3: Process nodes with zero in-degree
    while zero_in_degree_queue:
        u = zero_in_degree_queue.popleft()
        topological_order.append(u)
        
        # Decrease the in-degree of neighbor nodes
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zero_in_degree_queue.append(v)
    
    # If topological order includes all vertices, return it
    if len(topological_order) == len(graph):
        return topological_order
    else:
        # Graph has a cycle
        return []
```
```