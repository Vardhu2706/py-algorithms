# Fibonacci Algorithm

```python
```python
# Fibonacci Algorithm

## 1. Category / Type
"""
The Fibonacci algorithm belongs to the category of Dynamic Programming and Recursion.
It is a classic example often used to demonstrate these concepts.
"""

## 2. Core Idea / Intuition
"""
The core idea behind the Fibonacci algorithm is to generate a sequence where each number 
is the sum of the two preceding ones, starting from 0 and 1. 
Mathematically, the sequence is defined by the recurrence relation:
    F(n) = F(n-1) + F(n-2)
with seed values:
    F(0) = 0, F(1) = 1.
The intuition is to build up the solution for a given `n` by combining the solutions of subproblems `n-1` and `n-2`.
"""

## 3. Steps / Flow
"""
1. **Base Case Check**: 
   - If `n` is 0, return 0.
   - If `n` is 1, return 1.
   
2. **Recursive Calculation**:
   - Use the relation F(n) = F(n-1) + F(n-2) to recursively calculate Fibonacci numbers.

3. **Iterative Approach**:
   - Alternatively, an iterative approach can be used to avoid the overhead of recursive calls.
   - Initialize two variables to store the previous two Fibonacci numbers.
   - Iteratively update these variables until reaching the desired `n`.

4. **Dynamic Programming Approach**:
   - Use an array to store previously calculated Fibonacci numbers to avoid redundant calculations.
   - Fill the array iteratively up to the desired `n`.
"""

## 4. Time & Space Complexity
"""
| Best | Average | Worst | Space |
|------|---------|-------|-------|
| O(1) | O(n)    | O(n)  | O(n)  |
Note: The naive recursive solution has an exponential time complexity of O(2^n),
but using dynamic programming or iterative approaches reduces it to O(n).
"""

## 5. Use Cases
"""
- Fibonacci sequences are used in computer algorithms, financial models, and stock market analysis.
- They appear in biological settings, such as branching in trees, the arrangement of leaves on a stem, and the fruit sprouts of a pineapple.
"""

## 6. Common Variants
"""
- **Recursive Fibonacci**: Classic recursive approach.
- **Iterative Fibonacci**: Uses iteration to calculate the Fibonacci sequence.
- **Dynamic Programming Fibonacci**: Stores intermediate results to optimize performance.
- **Matrix Exponentiation**: Uses matrix representation to achieve O(log n) time complexity.
"""

## 7. Trade-offs
"""
- **Recursive vs Iterative**: Recursive is easier to implement but less efficient due to repeated calculations and call stack overhead.
- **Space Complexity**: Iterative and optimized dynamic programming approaches use less space compared to storing all Fibonacci numbers.
- **Performance**: Dynamic programming and matrix exponentiation improve time complexity significantly over naive recursion.
"""

## 8. Pitfalls / Gotchas
"""
- **Stack Overflow**: Recursive approach can lead to stack overflow for large `n` due to deep recursion.
- **Integer Overflow**: Large Fibonacci numbers can exceed standard integer limits in some languages.
- **Efficiency**: Naive recursive implementation is highly inefficient for large `n`.
"""

## 9. Classic Problems
"""
- Fibonacci sequence is a fundamental example in teaching recursion and dynamic programming.
- It is often used as an introductory problem in competitive programming and algorithm courses.
"""

## 10. Code Implementation (Demo)

def fibonacci(n):
    """Calculate the nth Fibonacci number using an iterative approach."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```
```