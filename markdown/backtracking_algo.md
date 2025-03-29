# Backtracking Algorithm

```python
```python
# Backtracking Algorithm

## 1. Category / Type
"""
Backtracking is a type of recursive algorithm used for solving constraint satisfaction problems, combinatorial optimization problems, and other search problems. It belongs to the category of depth-first search algorithms.
"""

## 2. Core Idea / Intuition
"""
The core idea of backtracking is to build a solution incrementally, one piece at a time, and remove solutions that fail to satisfy the constraints of the problem as soon as they are identified. This approach is often described as "exploring the decision tree" where the algorithm explores branches and backtracks when a branch does not lead to a viable solution.
"""

## 3. Steps / Flow
"""
1. Choose: Select the next element or decision to explore.
2. Explore: Recursively attempt to build a valid solution by adding the chosen element.
3. Backtrack: If the current solution path is invalid or complete, undo the last step (backtrack) and try a different option.
4. Repeat: Continue this process until all possibilities have been explored or a valid solution is found.
"""

## 4. Time & Space Complexity
"""
| Best      | Average   | Worst     | Space       |
|-----------|-----------|-----------|-------------|
| Varies    | Varies    | O(b^d)    | O(d)        |

- The time complexity is highly problem-specific. In general, it is O(b^d), where 'b' is the branching factor (number of choices at each step), and 'd' is the depth of the decision tree.
- The space complexity is O(d) due to the call stack from recursion.
"""

## 5. Use Cases
"""
- Solving puzzles like Sudoku and N-Queens
- Generating permutations and combinations
- Pathfinding in mazes
- Constraint satisfaction problems like graph coloring
"""

## 6. Common Variants
"""
- Pruning: Involves cutting off branches of the decision tree that are unlikely to lead to a solution.
- Branch and Bound: A technique that involves exploring branches based on potential lower bounds for optimization problems.
- Depth-First Search with Backtracking: A simpler version where the backtrack is simply a return from a recursive call.
"""

## 7. Trade-offs
"""
- Pros: Can find all possible solutions and is straightforward to implement.
- Cons: Can be inefficient for large problem spaces due to its exhaustive nature. May require optimization techniques like pruning to improve efficiency.
"""

## 8. Pitfalls / Gotchas
"""
- Inefficiency: Without optimization, backtracking can be too slow for large problems.
- Stack Overflow: Recursive implementations can lead to stack overflow if the recursion depth is too high.
- Missing pruning optimizations can lead to exploring unnecessary branches.
"""

## 9. Classic Problems
"""
- N-Queens Problem
- Sudoku Solver
- Crossword Puzzle Solver
- Hamiltonian Path Problem
"""

## 10. Code Implementation (Demo)
def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    # base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution then
            # remove queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this column col then return false
    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False

    # Print the solution
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    return True

# Example usage:
solve_n_queens(4)
```
```