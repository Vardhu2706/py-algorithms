# A* Search Algorithm

## 1. Category / Type
"""
- Pathfinding Algorithm
- Graph Search Algorithm
- Informed Search Algorithm
"""

## 2. Core Idea / Intuition
"""
A* Search Algorithm is designed to find the shortest path from a starting node to a target node in a graph. 
It combines features of both Dijkstra's Algorithm and Greedy Best-First Search. A* evaluates nodes by 
combining the cost to reach the node and a heuristic estimate of the cost to reach the goal from the node.
The key formula used by A* is:
    f(n) = g(n) + h(n)
where:
- f(n) is the total estimated cost of the cheapest path through node n.
- g(n) is the cost to reach node n from the start node.
- h(n) is the heuristic estimate to reach the goal from node n.
The heuristic function h(n) is problem-specific and should be admissible (never overestimate the true cost).
"""

## 3. Steps / Flow
"""
1. Initialize two sets: open_set (nodes to be evaluated) and closed_set (nodes already evaluated).
2. Add the starting node to the open_set.
3. While the open_set is not empty:
   a. Find the node with the lowest f(n) value in the open_set. Let's call this node 'current'.
   b. If 'current' is the goal node, reconstruct and return the path from start to goal.
   c. Remove 'current' from the open_set and add it to the closed_set.
   d. For each neighbor of 'current':
      i. If the neighbor is in the closed_set, skip to the next neighbor.
      ii. Calculate tentative_g_score for the neighbor.
      iii. If the neighbor is not in the open_set or the tentative_g_score is lower than the previously recorded score:
          - Update the neighbor's g_score and f_score.
          - Set the current node as the neighbor's parent.
          - If the neighbor is not in the open_set, add it.
4. If the goal node is not reached and open_set is empty, return failure indicating no path exists.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space  |
|---------|---------|---------|--------|
| O(1)    | O(b^d)  | O(b^d)  | O(b^d) |
- b: branching factor (average number of successors per state)
- d: depth of the least-cost solution
- The complexities are dependent on the heuristic function used.
"""

## 5. Use Cases
"""
- Navigation and route planning systems such as GPS.
- AI for games to find paths avoiding obstacles.
- Robotics for pathfinding in dynamic environments.
- Solving puzzles like the sliding puzzle or the traveling salesman problem.
"""

## 6. Common Variants
"""
- Dijkstra's Algorithm: A* without a heuristic (h(n) = 0).
- Greedy Best-First Search: A* with g(n) = 0.
- Weighted A*: Modifies the heuristic function to speed up the search at the cost of optimality.
- Iterative Deepening A*: Combines A* with Iterative Deepening Depth-First Search to reduce memory usage.
"""

## 7. Trade-offs
"""
- A* provides an optimal and complete solution if the heuristic is admissible and consistent.
- Memory usage can be high due to storing all explored nodes.
- Performance heavily depends on the choice of the heuristic function.
- Balancing between optimality (finding the shortest path) and speed (computational efficiency) is critical.
"""

## 8. Pitfalls / Gotchas
"""
- A poor heuristic can degrade the performance to that of an uninformed search like Dijkstra's.
- Ensuring the heuristic is admissible is crucial; otherwise, A* may not find the optimal path.
- Handling large graphs can lead to high memory consumption.
- A* may not be suitable for real-time applications with strict time constraints.
"""

## 9. Classic Problems
"""
- Eight Puzzle and Fifteen Puzzle: Finding the shortest sequence of moves to reach the goal state.
- Pathfinding in grids or maps: Commonly used in 2D grid-based games and simulations.
- Network routing: Finding the shortest path in communication networks.
- Robot motion planning: Navigating robots in an environment with obstacles.
"""

## 10. Code Implementation (Demo)
def astar_search(graph, start, goal, heuristic):
    open_set = {start}
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])
        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return "Failure: No path found"

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]
