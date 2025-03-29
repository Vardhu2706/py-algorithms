# Greedy Algorithms Algorithm

```python
```python
# Greedy Algorithms

## 1. Category / Type
"""
Greedy algorithms fall under the category of optimization and decision-making algorithms. They are commonly used in situations where a solution must be constructed incrementally with locally optimal choices.
"""

## 2. Core Idea / Intuition
"""
The core idea behind greedy algorithms is to solve problems by making a sequence of choices, each of which looks the best at the moment. The algorithm does not consider the global optimal solution but chooses the local optimum, assuming that it will lead to a globally optimal solution. This approach is effective when a problem exhibits the greedy-choice property and optimal substructure.
"""

## 3. Steps / Flow
"""
1. **Define the Problem**: Identify the problem and determine if it can be broken down into subproblems.
2. **Identify the Greedy Strategy**: Determine a strategy for making the locally optimal choice at each step.
3. **Prove the Greedy-Choice Property**: Show that a locally optimal choice leads to a globally optimal solution.
4. **Prove Optimal Substructure**: Demonstrate that the problem can be broken down into optimal subproblems.
5. **Implement the Algorithm**: Use the strategy to construct a solution incrementally, making the greedy choice at each step.
"""

## 4. Time & Space Complexity
"""
| Best       | Average    | Worst      | Space       |
|------------|------------|------------|-------------|
| Problem-specific | Problem-specific | Problem-specific | Problem-specific |

Note: The time and space complexity of greedy algorithms depend on the specific problem being solved. Each problem may have different complexities based on how the greedy choices are implemented and evaluated.
"""

## 5. Use Cases
"""
Greedy algorithms are used in various applications where a locally optimal choice leads to a globally optimal solution, such as:

- **Activity Selection Problem**: Scheduling maximum number of non-overlapping activities.
- **Huffman Coding**: Efficient data compression.
- **Prim's and Kruskal's Algorithms**: Finding minimum spanning trees in graphs.
- **Dijkstra's Algorithm**: Finding the shortest path in a graph with non-negative weights.
"""

## 6. Common Variants
"""
Common variants of greedy algorithms include:

- **Fractional Knapsack Problem**: Items can be divided, and the goal is to maximize the total value in the knapsack.
- **Coin Change Problem**: Finding the minimum number of coins needed to make a certain amount of change.
- **Job Sequencing Problem**: Scheduling jobs to maximize profit with deadlines.
"""

## 7. Trade-offs
"""
- **Pros**:
  - Simple to implement and understand.
  - Often faster than other algorithms due to reduced complexity.
  
- **Cons**:
  - Does not always produce the optimal solution for all problems.
  - Requires proof of correctness for each specific application.
"""

## 8. Pitfalls / Gotchas
"""
- Greedy algorithms can be misleading if the greedy-choice property and optimal substructure are not thoroughly verified.
- They may lead to suboptimal solutions if applied to problems not suited for the greedy approach.
- Overlooking boundary conditions and edge cases can lead to incorrect solutions.
"""

## 9. Classic Problems
"""
Some classic problems that are frequently solved using greedy algorithms include:

- **Minimum Spanning Tree**: Using Prim's or Kruskal's algorithm.
- **Shortest Path Problem**: Dijkstra's algorithm for graphs with non-negative weights.
- **Interval Partitioning**: Scheduling problems like the activity selection problem.
- **Optimal Merge Pattern**: To merge files with minimum total computation.
"""

## 10. Code Implementation (Demo)
"""
Below is a demonstration of a greedy algorithm solving the activity selection problem, where the goal is to select the maximum number of non-overlapping activities.

The activities are assumed to be sorted by their finish times. This is a common precondition for the greedy choice in this problem.

The function `activity_selection` takes a list of tuples, where each tuple contains the start and end time of an activity.

Example:
activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
The function returns the maximum set of non-overlapping activities.
"""

def activity_selection(activities):
    # Sort activities by their finish times
    activities.sort(key=lambda x: x[1])
    
    # The first activity always gets selected
    selected_activities = [activities[0]]
    
    # Iterate through the sorted activities
    for i in range(1, len(activities)):
        # If this activity starts after the last selected one ends, select it
        if activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(activities[i])
    
    return selected_activities

# Example usage
activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
print(activity_selection(activities))
```
```