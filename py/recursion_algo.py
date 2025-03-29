# Recursion Algorithm

## 1. Category / Type
"""
Recursion belongs to the category of algorithm design paradigms and techniques. It is a method of solving problems by breaking them down into smaller subproblems of the same type.
"""

## 2. Core Idea / Intuition
"""
The core idea of recursion is to solve a problem by reducing it to a simpler version of the same problem. This is accomplished by having functions call themselves with modified parameters, progressively moving towards a base case that terminates the recursive calls. Recursion leverages the call stack to keep track of function calls, allowing each recursive call to work with its own set of variables and parameters.
"""

## 3. Steps / Flow
"""
1. Define the base case: Identify a simple case for which the solution is known and does not require further recursion.
2. Define the recursive case: Express the solution of the problem in terms of smaller instances of the same problem.
3. Ensure convergence: Ensure that each recursive step brings the problem closer to the base case.
4. Execute: Call the recursive function with an appropriate initial argument to start the process.
5. Termination: The recursion terminates when the base case is reached, and results are propagated back through the call stack.
"""

## 4. Time & Space Complexity
"""
| Best       | Average    | Worst      | Space       |
|------------|------------|------------|-------------|
| O(1)       | Varies     | Exponential| O(n)        |
- The time complexity varies widely depending on the problem being solved.
- Space complexity is generally O(n) due to the call stack, where n is the depth of the recursion.
"""

## 5. Use Cases
"""
- Solving problems that can naturally be divided into smaller, similar subproblems, such as the Fibonacci sequence, factorial calculation, and tree traversals.
- Implementing algorithms that operate on hierarchical data structures like graphs and trees.
- Simplifying complex problems that have a recursive mathematical formulation.
"""

## 6. Common Variants
"""
- Tail Recursion: A specific type of recursion where the recursive call is the last statement in the function.
- Mutual Recursion: When two or more functions are recursive through each other.
- Indirect Recursion: A variant where a function calls another function that eventually calls the original function.
"""

## 7. Trade-offs
"""
- Pros:
  - Simplifies code for problems that have a recursive structure.
  - Often makes the code easier to read and understand.
- Cons:
  - Can be less efficient due to large memory overhead from the call stack.
  - May lead to stack overflow if the recursion depth is too large.
"""

## 8. Pitfalls / Gotchas
"""
- Stack Overflow: Deep recursion can lead to stack overflow errors due to limited stack space.
- Infinite Recursion: Failing to reach or correctly define the base case can lead to infinite recursion.
- Performance: Recursive solutions can be less efficient than iterative ones due to repeated calculations, although this can be mitigated using techniques like memoization.
"""

## 9. Classic Problems
"""
- Factorial calculation
- Fibonacci sequence
- Tower of Hanoi
- Merge Sort and Quick Sort
- Tree and Graph traversals (DFS, BFS)
"""

## 10. Code Implementation (Demo)
def factorial(n):
    """ Calculates the factorial of a number using recursion. """
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case
