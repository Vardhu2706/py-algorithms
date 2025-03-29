# Bubble Sort Algorithm

## 1. Category / Type
"""
Bubble Sort is a simple comparison-based sorting algorithm.
"""

## 2. Core Idea / Intuition
"""
The core idea of Bubble Sort is to repeatedly step through the list to be sorted, 
compare adjacent elements, and swap them if they are in the wrong order. This process 
is repeated until no more swaps are needed, indicating that the list is sorted.

The name "Bubble Sort" comes from the way larger elements "bubble" to the end of the 
list after each pass.
"""

## 3. Steps / Flow
"""
1. Start at the beginning of the list.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next element and repeat steps 2-3 until the end of the list is reached.
5. After each full pass through the list, the next largest element is in its correct position, 
   so reduce the range of the next pass by one.
6. Repeat the process for the entire list until a pass is completed without any swaps.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space |
|---------|---------|---------|-------|
| O(n)    | O(n^2)  | O(n^2)  | O(1)  |

- Best Case: O(n), occurs when the list is already sorted.
- Average and Worst Case: O(n^2), occurs when the list is in reverse order.
- Space Complexity: O(1), as Bubble Sort is an in-place sorting algorithm.
"""

## 5. Use Cases
"""
- Educational purposes to introduce the concept of sorting algorithms.
- Suitable for small datasets where implementation simplicity is more important than performance.
"""

## 6. Common Variants
"""
1. Optimized Bubble Sort: Includes a flag to monitor whether elements were swapped during a pass. If no swaps occur, the algorithm can terminate early.
2. Bidirectional Bubble Sort (Cocktail Shaker Sort): A variation that sorts in both directions on each pass through the list.
"""

## 7. Trade-offs
"""
- Simplicity vs. Efficiency: Bubble Sort is easy to implement and understand but inefficient for large datasets.
- Stability: Bubble Sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements.
"""

## 8. Pitfalls / Gotchas
"""
- Inefficiency for large datasets: Due to its O(n^2) average and worst-case time complexity, Bubble Sort is impractical for large lists.
- Misuse in performance-critical applications: Avoid using Bubble Sort in scenarios where performance is a critical factor.
"""

## 9. Classic Problems
"""
- Sorting small datasets or nearly sorted datasets.
- Educational demonstrations of sorting concepts.
"""

## 10. Code Implementation (Demo)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
