# Interval Scheduling Algorithm

## 1. Category / Type
"""
Greedy Algorithm
"""

## 2. Core Idea / Intuition
"""
The core idea of the Interval Scheduling algorithm is to select the maximum number of non-overlapping intervals from a set of intervals. The greedy strategy is to always pick the interval that finishes the earliest, as this leaves the most room for future intervals. By sorting the intervals by their end times and iteratively selecting intervals that start after the last selected one ends, we can efficiently build an optimal solution.
"""

## 3. Steps / Flow
"""
1. **Sort Intervals**: Begin by sorting the list of intervals based on their end times.
2. **Initialize**: Start with an empty schedule and a variable to keep track of the end time of the last added interval.
3. **Iterate Through Intervals**:
   - For each interval in the sorted list:
     - If the start time of the current interval is greater than or equal to the end time of the last added interval, add this interval to the schedule.
     - Update the end time to the end time of the current interval.
4. **Output**: The schedule now contains the maximum number of non-overlapping intervals.
"""

## 4. Time & Space Complexity
"""
| Best     | Average | Worst     | Space |
|----------|---------|-----------|-------|
| O(n log n) | O(n log n) | O(n log n) | O(n) |
"""

## 5. Use Cases
"""
- Scheduling tasks in a single machine to maximize tasks executed without overlap.
- Allocating resources like meeting rooms or CPU slots where tasks require exclusive access.
- Optimizing advertisement slots where each ad has a set start and end time.
"""

## 6. Common Variants
"""
- Weighted Interval Scheduling: Each interval has a weight, and the objective is to maximize the total weight.
- Interval Partitioning: Minimize the number of resources needed for overlapping intervals.
- Maximum Length of Non-overlapping Intervals: Instead of the count, maximize the total length of selected intervals.
"""

## 7. Trade-offs
"""
- The algorithm is optimal for the unweighted version but doesn't account for interval lengths or values.
- Requires sorting, which can be computationally expensive for very large datasets.
- Assumes all intervals are available beforehand and are static, which may not be practical in dynamic environments.
"""

## 8. Pitfalls / Gotchas
"""
- Ensure intervals are correctly sorted by end time; otherwise, the greedy choice may not yield an optimal solution.
- Be cautious of intervals with equal end times; any selection among them is valid.
- Handle edge cases like intervals with zero length or fully overlapping intervals.
"""

## 9. Classic Problems
"""
- Activity Selection Problem: A classic problem where the goal is to select the maximum number of activities that don't overlap.
- Job Scheduling with Deadlines: Ensuring jobs are completed by their deadlines without overlap.
- Train Platform Scheduling: Allocating the minimum number of platforms for arriving trains.
"""

## 10. Code Implementation (Demo)
def interval_scheduling(intervals):
    # Sort intervals based on their end times
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    # Initialize the list to store the selected intervals
    selected_intervals = []
    
    # Initialize the end time of the last selected interval
    last_end_time = float('-inf')
    
    # Iterate through sorted intervals
    for start, end in sorted_intervals:
        # If the current interval starts after or when the last selected one ends
        if start >= last_end_time:
            # Add the current interval to the selected list
            selected_intervals.append((start, end))
            # Update the end time of the last selected interval
            last_end_time = end
    
    return selected_intervals

# Example usage
intervals = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7), (8, 9)]
print(interval_scheduling(intervals))
