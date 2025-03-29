# Bucket Sort Algorithm

## 1. Category / Type
"""
Bucket Sort is a distribution sort that distributes elements into a number of buckets, sorts these buckets individually, and then combines them.
"""

## 2. Core Idea / Intuition
"""
The core idea of Bucket Sort is to divide the input data into several 'buckets', which are then sorted individually, either using another sorting algorithm or by recursively applying the bucket sorting process. 

The assumption is that input data is uniformly distributed over a range, and this characteristic can be leveraged to sort the data efficiently.

The intuition behind Bucket Sort is to reduce the number of comparisons needed to sort the entire dataset by reducing the problem size into smaller, more manageable pieces.
"""

## 3. Steps / Flow
"""
1. **Create Buckets**: Create an empty list of buckets.
2. **Distribute Elements**: Iterate through the input list, and distribute each element into its respective bucket based on a hashing function.
3. **Sort Buckets**: Sort each non-empty bucket. This can be done using any sorting algorithm, but insertion sort is commonly used for its efficiency on small datasets.
4. **Concatenate Buckets**: Concatenate the sorted buckets to form the final sorted array.

These steps leverage the assumption that sorting smaller lists (buckets) is more efficient than sorting one large list.
"""

## 4. Time & Space Complexity
"""
| Best     | Average | Worst   | Space   |
|----------|---------|---------|---------|
| O(n + k) | O(n + k)| O(n^2)  | O(n + k)|

- `n` is the number of elements to be sorted.
- `k` is the number of buckets.
- The worst-case time complexity occurs when all elements are placed into a single bucket.
"""

## 5. Use Cases
"""
- Suitable for sorting data that is uniformly distributed over a known range.
- Useful in cases where auxiliary space is available and efficient distribution of data into buckets can be achieved.
- Example applications include sorting a large number of floating-point numbers that lie within a specific range.
"""

## 6. Common Variants
"""
- **Parallel Bucket Sort**: A parallelized version of bucket sort that distributes buckets across multiple processors for concurrent sorting.
- **Radix Bucket Sort**: Combines bucket sort with radix sort, using bucket sort for each digit or group of digits.
"""

## 7. Trade-offs
"""
- **Pros**:
  - Linear time complexity in the best and average cases when data is uniformly distributed.
  - Simple and intuitive approach for certain types of data.
  
- **Cons**:
  - Poor performance if elements are not uniformly distributed.
  - Requires additional space for buckets.
  - Choice of bucket count can significantly affect performance.
"""

## 8. Pitfalls / Gotchas
"""
- The efficiency of bucket sort is highly dependent on the distribution of the input data. If the data is not evenly distributed, performance may degrade to O(n^2).
- Choosing the right number of buckets is critical; too few buckets can lead to inefficiencies, while too many can increase overhead.
- Bucket Sort is not a comparison-based algorithm, so it is not useful for generic comparison operations.
"""

## 9. Classic Problems
"""
- Sorting floating point numbers between 0 and 1.
- Sorting large datasets where data is expected to be uniformly distributed over a known range.
"""

## 10. Code Implementation (Demo)
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Create buckets
    bucket_count = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    bucket_size = (max_value - min_value) / bucket_count

    buckets = [[] for _ in range(bucket_count)]

    # Step 2: Distribute elements into buckets
    for num in arr:
        index = int((num - min_value) / bucket_size)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)

    # Step 3: Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Step 4: Concatenate buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array
