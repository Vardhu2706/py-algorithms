# N-Queens Algorithm

```python
```python
# N-Queens Algorithm

## 1. Category / Type
"""
The N-Queens algorithm is a classic example of a backtracking algorithm.
"""

## 2. Core Idea / Intuition
"""
The core idea of the N-Queens problem is to place N queens on an N×N chessboard such that no two queens threaten each other. 
This means that no two queens can share the same row, column, or diagonal. The algorithm uses backtracking to explore all 
possible positions of the queens and backtracks whenever a conflict is detected.
"""

## 3. Steps / Flow
"""
1. Start in the leftmost column.
2. If all queens are placed, return true.
3. Try all rows in the current column. For each row, do the following:
   a. If the queen can be safely placed in this row, place the queen and mark this cell on the board.
   b. Recurse to place the rest of the queens.
   c. If placing the queen in the current position leads to a solution, return true.
   d. If placing the queen in the current position does not lead to a solution, remove the queen (backtrack) and try the next row.
4. If all rows have been tried and no solution is found in the current column, return false.
"""

## 4. Time & Space Complexity
"""
|   Best  | Average |  Worst  | Space |
|---------|---------|---------|-------|
| O(N!)   | O(N!)   | O(N!)   | O(N)  |
The time complexity is O(N!) because there are N possibilities for each queen for N queens, resulting in a factorial growth. 
The space complexity is O(N) due to the recursion stack and the space required to store the positions of queens.
"""

## 5. Use Cases
"""
- Solving puzzles and games that involve grid-based constraints.
- Used in constraint satisfaction problems.
- Useful in scenarios requiring combinatorial search and optimization.
"""

## 6. Common Variants
"""
- 8-Queens is a specific case of the N-Queens problem with N=8.
- N-Rooks problem, where rooks replace queens, requiring only column and row constraints.
- N-Knights problem, involving knights rather than queens.
"""

## 7. Trade-offs
"""
- The problem has an exponential time complexity, making it inefficient for very large N.
- Backtracking is a brute-force approach but is more efficient than generating all permutations of board arrangements.
- Memory usage is generally low, but stack overflow can occur with very large N due to deep recursion.
"""

## 8. Pitfalls / Gotchas
"""
- Ensuring that the diagonal constraints are correctly implemented is crucial and can be a common source of errors.
- The algorithm assumes an empty chessboard; care must be taken if there are pre-existing constraints.
"""

## 9. Classic Problems
"""
- The N-Queens problem itself is a classic problem in computer science and is often used to illustrate backtracking techniques.
- Related classic problems include Sudoku solving and other constraint satisfaction problems.
"""

## 10. Code Implementation (Demo)
def solveNQueens(N):
    def is_safe(board, row, col):
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check lower diagonal on the left side
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, col):
        if col >= N:
            solutions.append([''.join(row) for row in board])
            return True

        res = False
        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                res = solve(board, col + 1) or res
                board[i][col] = '.'  # backtrack

        return res

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0)
    return solutions

# Example usage
print(solveNQueens(4))
```
```