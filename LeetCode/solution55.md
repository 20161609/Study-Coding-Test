> 2025.01.05
> 

### [Jump Game - LeetCode](https://leetcode.com/problems/jump-game/description/)

---

# Approach

1. **Problem Understanding**: The task is to determine whether it is possible to reach the last index starting from the first index in an array `nums`, where each element represents the maximum jump length at that position.
2. **Key Insight**: By keeping track of the maximum reachable index (`max_reachable`) as we iterate through the array, we can decide whether it is possible to progress further or not.
3. **Algorithm**:
    - Start with `max_reachable = 0`.
    - Iterate through each index `i` and its value `num` in `nums`.
    - If `i > max_reachable`, return `False` (current position is not reachable).
    - Update `max_reachable` to the maximum of its current value and `i + num`.
    - If the loop completes without returning `False`, return `True` (reaching the last index is possible).

---

# Code

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Max index to reach.
        max_reachable = 0
        for i, num in enumerate(nums):
            if i > max_reachable:
                # If current position 'i' is over the range of reachable indices.
                return False

            # Update max_reachable.
            max_reachable = max(max_reachable, i + num)
        return True

```

---

# Complexity Analysis

**Time Complexity**: `O(n)`

- We iterate through the array `nums` exactly once, where `n` is the length of `nums`.
- Each iteration performs constant-time operations (comparison and max update), leading to a linear time complexity.

**Space Complexity**: `O(1)`

- The solution uses a constant amount of additional space to store `max_reachable` and loop variables.
- No auxiliary data structures are used, so the space complexity is constant.

---

# Review

The algorithm is efficient and leverages a greedy approach to minimize unnecessary computations. It successfully handles edge cases such as:

- A single element in the array (`nums = [0]` → output: `True`).
- An array with all zeroes except the first element being non-zero (`nums = [3, 0, 0, 0]` → output: `True`).
- An array where reaching the last index is impossible (`nums = [3, 2, 1, 0, 4]` → output: `False`).

The greedy approach ensures that the solution is optimal with respect to both time and space.