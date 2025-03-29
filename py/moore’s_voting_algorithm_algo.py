# Moore's Voting Algorithm

## 1. Category / Type
"""
- Majority Element Detection
- Voting Algorithm
"""

## 2. Core Idea / Intuition
"""
Moore's Voting Algorithm is designed to find a majority element in a sequence of elements. 
A majority element is an element that appears more than n/2 times in an array of size n.
The core intuition behind the algorithm is to maintain a candidate for the majority element and 
a counter to keep track of its frequency relative to other elements. When encountering an element 
that matches the candidate, the counter is incremented; otherwise, it is decremented. 
When the counter reaches zero, the current element becomes the new candidate.

The algorithm is efficient because it only requires a single pass over the array (O(n) time complexity)
and uses O(1) space.
"""

## 3. Steps / Flow
"""
The algorithm operates in two primary phases:

1. **Candidate Selection Phase**:
   - Initialize a `candidate` variable to None and a `count` variable to 0.
   - Iterate through each element in the array:
     - If `count` is 0, set the `candidate` to the current element and set `count` to 1.
     - If the current element matches the `candidate`, increment `count`.
     - Otherwise, decrement `count`.

2. **Candidate Verification Phase**:
   - After the first pass, a candidate for the majority element is determined.
   - To confirm this candidate, iterate through the array once more and count its occurrences.
   - If the count of the `candidate` is greater than n/2, then it is indeed the majority element.
   - Otherwise, there is no majority element in the array.
"""

## 4. Time & Space Complexity
"""
| Best | Average | Worst | Space |
|------|---------|-------|-------|
| O(n) | O(n)    | O(n)  | O(1)  |
"""

## 5. Use Cases
"""
- Finding a majority vote in elections or polls where a candidate must have more than half the votes.
- Detecting a dominant element in data streams or large datasets efficiently.
- Simplifying the problem of balancing decisions or preferences in distributed systems.
"""

## 6. Common Variants
"""
- The algorithm can be adapted to find elements that appear more than n/k times by maintaining more than one candidate.
- Extended versions can track additional data for weighted voting scenarios.
"""

## 7. Trade-offs
"""
- This algorithm assumes that a majority element always exists; if this condition is not met, 
  the algorithm may return a false candidate unless verified.
- The verification step is necessary to confirm the candidate, which requires an additional pass through the array.
- It is not suitable for detecting elements that appear more than n/k times if k > 2.
"""

## 8. Pitfalls / Gotchas
"""
- Failing to verify the candidate can lead to incorrect results if no majority element exists.
- Care must be taken to reset the candidate properly when the count reaches zero.
- The algorithm assumes that the input size is at least one; handling empty inputs needs special attention.
"""

## 9. Classic Problems
"""
- Finding the majority element in a list of votes or survey results.
- Identifying the most common element in real-time data streams.
- Used in problems like finding the most common color in an image, where colors can be represented as elements.
"""

## 10. Code Implementation (Demo)

def moores_voting_algorithm(arr):
    candidate, count = None, 0
    
    # Candidate Selection Phase
    for num in arr:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Candidate Verification Phase
    count = sum(1 for num in arr if num == candidate)
    
    if count > len(arr) // 2:
        return candidate
    return None

# Example Usage:
# arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# result = moores_voting_algorithm(arr)
# print(result)  # Output: 4
