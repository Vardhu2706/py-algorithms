# Depth First Search (DFS) Algorithm

## 1. Category / Type
"""
- Graph Traversal
- Search Algorithms
"""

## 2. Core Idea / Intuition
"""
Depth First Search (DFS) is a fundamental algorithm used to explore nodes and edges of a graph. 
The core idea is to start at the root (or an arbitrary node), explore as far along each branch as possible before backtracking.
This approach uses a stack (LIFO) data structure, either explicitly through an iterative process or implicitly via recursion.
DFS is particularly useful for scenarios where we need to explore all possibilities, such as puzzle solving, and is instrumental in topological sorts, cycle detection, and pathfinding in mazes.
"""

## 3. Steps / Flow
"""
1. Start at the root node (or any arbitrary node in the case of a disconnected graph).
2. Mark the starting node as visited.
3. Push the starting node onto a stack.
4. While the stack is not empty:
   a. Pop the top node from the stack.
   b. Process this node (e.g., print it, check for a condition).
   c. Retrieve all adjacent, unvisited nodes of the current node.
   d. For each unvisited adjacent node, mark it as visited and push it onto the stack.
5. Repeat until the stack is empty, indicating all reachable nodes have been processed.
"""

## 4. Time & Space Complexity
"""
| Best | Average | Worst | Space |
|------|---------|-------|-------|
| O(V + E) | O(V + E) | O(V + E) | O(V)  |
Where V is the number of vertices and E is the number of edges in the graph.
The time complexity arises because, in the worst case, every vertex and every edge will be explored.
The space complexity is O(V) due to the storage required for the stack and the visited list.
"""

## 5. Use Cases
"""
- Pathfinding algorithms and AI for games.
- Detecting cycles in a graph.
- Solving puzzles with backtracking, such as Sudoku.
- Topological sorting in a directed graph.
- Finding connected components in a graph.
"""

## 6. Common Variants
"""
- Iterative DFS using an explicit stack.
- Recursive DFS utilizing the call stack.
- Depth-Limited Search which limits the depth of the DFS tree.
- Iterative Deepening DFS, which combines the space efficiency of BFS with the depth-first nature of DFS.
"""

## 7. Trade-offs
"""
- DFS can be more memory-efficient than Breadth-First Search (BFS) for deep graphs since it only needs to store a single path from the root to a leaf node, along with unexplored siblings for each node.
- However, DFS does not guarantee the shortest path in unweighted graphs, unlike BFS.
- It can get trapped in cyclic graphs or infinite depths without proper cycle checks or depth limits.
"""

## 8. Pitfalls / Gotchas
"""
- Without careful cycle detection, DFS can enter infinite loops in cyclic graphs.
- Recursive DFS might lead to a stack overflow for very deep graphs.
- DFS does not find the shortest path in graphs with uniform edge weights.
"""

## 9. Classic Problems
"""
- Maze Solving Problem.
- Finding Strongly Connected Components (Tarjan's or Kosaraju's algorithm).
- Topological Sorting of a Directed Acyclic Graph (DAG).
- Checking if a graph is bipartite.
"""

## 10. Code Implementation (Demo)
def dfs(graph, start):
    """
    Perform a depth-first search on a graph from a start node.

    :param graph: A dictionary representing the adjacency list of the graph.
    :param start: The starting node for the DFS traversal.
    :return: A list of nodes in the order they were visited.
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add adjacent nodes in reverse order to maintain order of traversal
            stack.extend(reversed(graph[node]))

    return result

# Example usage:
graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(dfs(graph_example, 'A'))  # Output: ['A', 'C', 'F', 'B', 'E', 'D']
