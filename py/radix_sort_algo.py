# Radix Sort Algorithm

## 1. Category / Type
"""
Radix Sort is a non-comparative integer sorting algorithm. It is categorized under distribution sorts.
"""

## 2. Core Idea / Intuition
"""
The core idea of Radix Sort involves sorting numbers digit by digit starting from the least significant digit (LSD) to the most significant digit (MSD). It uses a stable sub-sorting algorithm (often counting sort) to sort the numbers at each digit level.

The intuition is that by sorting numbers based on individual digit significance, starting from the least, we can progressively build up a sorted list. This method leverages the positional representation of numbers, making it particularly efficient for fixed-length integer keys.
"""

## 3. Steps / Flow
"""
1. Determine the maximum number in the list to know the number of digits.
2. Initialize the digit position to the least significant digit (LSD).
3. While there are digits to process:
   - Use a stable sorting algorithm (e.g., counting sort) to sort the list based on the current digit.
   - Move to the next more significant digit.
4. Repeat until the most significant digit (MSD) is processed.
"""

## 4. Time & Space Complexity
"""
| Best      | Average  | Worst    | Space   |
|-----------|----------|----------|---------|
| O(nk)     | O(nk)    | O(nk)    | O(n+k)  |

- n is the number of elements in the list.
- k is the number of digits in the longest number.
- The time complexity assumes that the sub-sorting algorithm (like counting sort) operates in O(n + k).
"""

## 5. Use Cases
"""
- Radix Sort is particularly useful for sorting large lists of integers, especially where the numbers have a fixed length.
- It is used in applications where the range of the number is not too large, making counting sort feasible for digit-level sorting.
"""

## 6. Common Variants
"""
- LSD Radix Sort: Processes digits from least significant to most significant.
- MSD Radix Sort: Processes digits from most significant to least significant. Often implemented using recursive approaches.
"""

## 7. Trade-offs
"""
- Radix Sort is efficient for sorting integers and fixed-length strings, but it is not suitable for floating-point numbers or negative numbers without modification.
- It requires extra space proportional to the number of elements and the base used for sorting, which might be significant.
- It is most effective when the number of digits (k) is significantly smaller than the number of elements to sort (n).
"""

## 8. Pitfalls / Gotchas
"""
- Radix Sort requires a stable sorting algorithm for digit-level sorting. If the sub-algorithm is not stable, the overall sort will not be correct.
- It is not a comparison-based sort, so it cannot be directly applied to data types other than integers.
- The choice of the base can affect performance; usually, base 10 or base 256 (for byte-wise sorting) is used.
"""

## 9. Classic Problems
"""
- Sorting telephone numbers, social security numbers, or any large set of integers efficiently.
- Digit-by-digit sorting of fixed-width strings or numbers.
"""

## 10. Code Implementation (Demo)
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)
