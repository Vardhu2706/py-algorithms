# Reservoir Sampling Algorithm

```python
```python
# Reservoir Sampling Algorithm

## 1. Category / Type
"""
Reservoir Sampling is a Randomized Algorithm.
"""

## 2. Core Idea / Intuition
"""
The core idea of the Reservoir Sampling algorithm is to randomly select `k` items from a stream of `n` items where `n` is either a very large number or unknown. The algorithm ensures each item in the stream has an equal probability of being chosen in the sample of size `k`.

The intuition behind the algorithm is to maintain a "reservoir" of size `k` and replace elements in this reservoir with elements from the stream with decreasing probability as the stream progresses. This approach allows processing of potentially infinite data streams with constant memory usage.
"""

## 3. Steps / Flow
"""
1. **Initialization**: 
   - Create an array `reservoir[]` of size `k` and fill it with the first `k` items from the stream.

2. **Iterate over the Stream**:
   - For each new item `i` from the `(k+1)`th item onward in the stream:
     - Generate a random integer `j` such that `0 <= j <= i`.
     - If `j` is less than `k`, replace `reservoir[j]` with the new item from the stream.

3. **Final Output**:
   - After processing all items in the stream, `reservoir[]` contains `k` randomly selected items.

This flow ensures that each item in the input stream has an equal chance of 1/n to be included in the reservoir.
"""

## 4. Time & Space Complexity
"""
| Best | Average | Worst | Space |
|------|---------|-------|-------|
| O(n) | O(n)    | O(n)  | O(k)  |
"""

## 5. Use Cases
"""
- Random sampling of `k` items from large datasets or data streams where the size of the data is too large to fit into memory.
- Situations where the data stream is potentially infinite or unbounded.
- Applications in statistics, machine learning, and data analysis where unbiased sampling is required.
"""

## 6. Common Variants
"""
- **Weighted Reservoir Sampling**: Each item has a different probability of being selected based on weights.
- **Distributed Reservoir Sampling**: Adaptations to handle distributed data streams across multiple nodes or systems.
"""

## 7. Trade-offs
"""
- **Pros**: 
  - Constant space complexity O(k), making it highly efficient for large streams.
  - Simple to implement with clear and concise logic.

- **Cons**:
  - Relies on a good source of randomness for fair sampling.
  - As `k` or the number of items in the stream grows, the time taken for random number generation and replacement operations increases linearly.
"""

## 8. Pitfalls / Gotchas
"""
- Ensuring proper random number generation is crucial; poor randomness can bias the reservoir.
- Misunderstanding the probability adjustment for reservoir replacement can lead to incorrect implementations.
"""

## 9. Classic Problems
"""
- Selecting a random sample of `k` lines from a file with unknown number of lines.
- Implementing fair sampling in streaming algorithms for real-time data.
"""

## 10. Code Implementation (Demo)
def reservoir_sampling(stream, k):
    import random

    # Step 1: Fill the reservoir array with the first k elements from the stream
    reservoir = []
    for i in range(k):
        reservoir.append(stream[i])
    
    # Step 2: Iterate over the rest of the elements in the stream
    n = len(stream)
    for i in range(k, n):
        # Generate a random index from 0 to i
        j = random.randint(0, i)
        
        # If the randomly picked index is smaller than k, replace the element
        if j < k:
            reservoir[j] = stream[i]
    
    return reservoir

# Example usage:
# stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 5
# print(reservoir_sampling(stream, k))
```
```