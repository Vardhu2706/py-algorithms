# Counting Sort Algorithm

```python
```python
# Counting Sort Algorithm

## 1. Category / Type
"""
Counting Sort is a non-comparison-based integer sorting algorithm.
"""

## 2. Core Idea / Intuition
"""
The core idea of Counting Sort is to count the occurrences of each unique element in the input list and use this information to determine the correct position of each element in the output sorted list. It is particularly efficient when the range of input values (k) is not significantly larger than the number of elements (n) to be sorted.

Counting Sort works by:
- Creating a count array to store the frequency of each element.
- Modifying the count array to store the cumulative sum of elements.
- Using the cumulative counts to place each element at its correct position in the output array.
"""

## 3. Steps / Flow
"""
1. **Initialize Count Array**: 
   - Determine the range of the input data (i.e., the maximum and minimum values).
   - Create a count array of size equal to the range of input data.

2. **Count Occurrences**:
   - Traverse the input array and increase the count of each element in the count array.

3. **Accumulate Counts**:
   - Modify the count array by adding the count of the previous element to each element. This step transforms the count array into a prefix sum array, storing the cumulative count of elements up to each index.

4. **Build Output Array**:
   - Iterate over the input array in reverse order.
   - Place each element at the position indicated by the count array in the output array.
   - Decrease the count of each element after placing it in the output array.

5. **Copy to Original Array** (optional):
   - Copy the sorted elements back to the original array if in-place sorting is desired.
"""

## 4. Time & Space Complexity
"""
| Best    | Average | Worst   | Space    |
|---------|---------|---------|----------|
| O(n+k)  | O(n+k)  | O(n+k)  | O(k+n)   |
- n is the number of elements in the input array.
- k is the range of the input (i.e., the difference between the maximum and minimum values).
"""

## 5. Use Cases
"""
- Sorting integers when the range of possible values is not significantly larger than the number of elements to be sorted.
- Situations where stability is required and the input consists of non-negative integers.
- Counting Sort is often used as a subroutine in more advanced algorithms like Radix Sort.
"""

## 6. Common Variants
"""
- **Stable Counting Sort**: The version implemented here, which maintains the relative order of equal elements.
- **In-place Counting Sort**: A variant that aims to reduce space complexity by sorting the array in place, albeit at the cost of stability.
"""

## 7. Trade-offs
"""
- **Advantages**:
  - Linear time complexity for small range of numbers.
  - Stable sort, maintaining the relative order of equal elements.
  - Suitable for sorting large arrays with small ranges.

- **Disadvantages**:
  - Not suitable for large range of numbers as it requires O(k) space.
  - Inefficient for non-integer data or when integer keys are widely spread.
"""

## 8. Pitfalls / Gotchas
"""
- Counting Sort is not a comparison-based sort, which means it can only be applied to data types that can be converted into discrete keys (typically integers).
- The algorithm's space complexity can become a problem when the range of the input values is large.
"""

## 9. Classic Problems
"""
- Sorting non-negative integers in O(n) time.
- Preprocessing step for Radix Sort.
"""

## 10. Code Implementation (Demo)
def counting_sort(arr):
    if not arr:
        return arr
    
    # Find the maximum element in the array
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    # Initialize count array
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Change count[i] so that count[i] now contains the actual position of this element in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build the output array using the count array
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    # Copy the sorted elements into the original array
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr
```
```