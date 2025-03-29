# Bit Manipulation Techniques Algorithm

## 1. Category / Type
"""
Bit Manipulation
"""

## 2. Core Idea / Intuition
"""
The core idea of bit manipulation is to perform operations directly on bits, which can be more efficient than using traditional arithmetic operations. Bit manipulation techniques take advantage of the binary representation of data to perform tasks such as setting, clearing, toggling, and checking the value of specific bits. These operations are typically faster because they are directly supported by the processor's instruction set.
"""

## 3. Steps / Flow
"""
1. **Setting a Bit**: To set a specific bit, use the OR operation. For example, to set the `i-th` bit of number `n`, use `n | (1 << i)`.

2. **Clearing a Bit**: To clear a specific bit, use the AND operation with the NOT of the bit mask. For example, to clear the `i-th` bit, use `n & ~(1 << i)`.

3. **Toggling a Bit**: To toggle a specific bit, use the XOR operation. For example, to toggle the `i-th` bit, use `n ^ (1 << i)`.

4. **Checking a Bit**: To check if a particular bit is set, use the AND operation. For example, `n & (1 << i)` will be non-zero if the `i-th` bit is set.

5. **Common Bit Manipulation Tricks**:
   - **Check if a number is even or odd**: Use `n & 1`. If the result is `0`, the number is even; if `1`, it is odd.
   - **Divide/Multiply by 2**: Use right shift `n >> 1` to divide and left shift `n << 1` to multiply by 2.
   - **Swapping two numbers**: Use XOR to swap two numbers without a temporary variable.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst | Space |
|---------|---------|-------|-------|
| O(1)    | O(1)    | O(1)  | O(1)  |
"""

## 5. Use Cases
"""
- Optimizing mathematical calculations by using bit-level operations.
- Efficiently handling flags or binary states within a program.
- Implementing low-level data processing algorithms, such as image processing or cryptography.
- Reducing space and time complexity in systems programming.
"""

## 6. Common Variants
"""
- **Gray Code**: A binary numeral system where two successive values differ in only one bit.
- **Bitmasking**: Using masks to extract or set specific bits.
- **Hamming Distance Calculation**: Measure of the difference between two strings of equal length.
"""

## 7. Trade-offs
"""
- **Readability vs. Performance**: While bit manipulation can significantly improve performance, it can also make the code less readable and harder to maintain.
- **Portability**: Bit manipulation assumes certain integer sizes and endianness, which can vary across platforms.
"""

## 8. Pitfalls / Gotchas
"""
- **Misunderstanding Bit Shifts**: Shifting bits too far can lead to unexpected results, especially with signed integers.
- **Sign Extension**: Right shifting negative numbers can result in sign extension, which may not be desired.
- **Integer Overflow**: Operations that exceed the maximum size of the integer can lead to overflow.
"""

## 9. Classic Problems
"""
- **Finding the single non-repeating element in an array where every other element repeats twice**.
- **Counting the number of 1 bits in an integer (Hamming Weight)**.
- **Determining if a number is a power of two**.
"""

## 10. Code Implementation (Demo)
def set_bit(n, i):
    """Sets the i-th bit of n."""
    return n | (1 << i)

def clear_bit(n, i):
    """Clears the i-th bit of n."""
    return n & ~(1 << i)

def toggle_bit(n, i):
    """Toggles the i-th bit of n."""
    return n ^ (1 << i)

def check_bit(n, i):
    """Checks if the i-th bit of n is set."""
    return (n & (1 << i)) != 0

def is_even(n):
    """Checks if the number is even."""
    return (n & 1) == 0

def multiply_by_two(n):
    """Multiplies the number by two."""
    return n << 1

def divide_by_two(n):
    """Divides the number by two."""
    return n >> 1

# Example usage:
# Setting the 3rd bit of 5 (0101 -> 1101)
print(set_bit(5, 3))  # Output: 13

# Clearing the 2nd bit of 5 (0101 -> 0101)
print(clear_bit(5, 2))  # Output: 5

# Toggling the 1st bit of 5 (0101 -> 0100)
print(toggle_bit(5, 1))  # Output: 4

# Checking the 0th bit of 5 (0101)
print(check_bit(5, 0))  # Output: True

# Check if 6 is even
print(is_even(6))  # Output: True

# Multiply 3 by two
print(multiply_by_two(3))  # Output: 6

# Divide 6 by two
print(divide_by_two(6))  # Output: 3
