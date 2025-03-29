# Sudoku Solver Algorithm

## 1. Category / Type
"""
- Backtracking Algorithm
- Constraint Satisfaction Problem
"""

## 2. Core Idea / Intuition
"""
The core idea behind the Sudoku Solver algorithm is to fill a 9x9 grid following Sudoku rules:
- Each row must contain the numbers 1-9 without repetition.
- Each column must contain the numbers 1-9 without repetition.
- Each of the nine 3x3 subgrids must also contain the numbers 1-9 without repetition.

The algorithm primarily uses backtracking to solve the puzzle. It attempts to place numbers in empty positions and checks if the current placement is valid. If a placement violates Sudoku rules, it backtracks and tries the next possibility until it finds a solution or exhausts all options.
"""

## 3. Steps / Flow
"""
1. Identify the first empty cell in the grid.
2. Attempt to place a number (1-9) in the identified cell.
3. For each number, check if it is valid:
   - The number is not already present in the current row.
   - The number is not already present in the current column.
   - The number is not already present in the corresponding 3x3 subgrid.
4. If a valid number is found, place it in the cell and recursively attempt to fill the rest of the grid.
5. If no valid number is found for a cell, backtrack to the previous cell and try the next number.
6. Repeat the process until the grid is completely filled or no solution is found.
"""

## 4. Time & Space Complexity
"""
| Best      | Average   | Worst     | Space    |
|-----------|-----------|-----------|----------|
| O(1)      | O((9!)^9) | O((9!)^9) | O(1)     |

- The best-case scenario occurs when the puzzle is already solved.
- The average and worst-case complexities are derived from the potential number of permutations that need to be checked in the worst-case scenario.
- Space complexity is constant as the algorithm modifies the input grid in place and uses a fixed amount of additional space.
"""

## 5. Use Cases
"""
- Solving standard 9x9 Sudoku puzzles.
- Can be adapted to solve larger or smaller Sudoku puzzles by adjusting grid and subgrid sizes.
- Useful in AI applications involving constraint satisfaction problems.
"""

## 6. Common Variants
"""
- Non-standard Sudoku grids (e.g., 16x16, 4x4).
- Sudoku puzzles with additional constraints (e.g., diagonal Sudoku).
"""

## 7. Trade-offs
"""
- The algorithm is simple and easy to implement but can be inefficient for puzzles with large search spaces.
- May run into performance issues with minimal initial clues due to extensive backtracking.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure the grid is a valid 9x9 matrix before attempting to solve.
- Be cautious of input validation to avoid index errors.
- Recursive depth can be high in complex puzzles, potentially leading to stack overflow in some environments.
"""

## 9. Classic Problems
"""
- Solving a Sudoku puzzle with the minimum number of given numbers.
- The N-Queens problem shares a similar backtracking approach.
"""

## 10. Code Implementation (Demo)
def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True
