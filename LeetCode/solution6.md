### [Zigzag Conversion - LeetCode](https://leetcode.com/problems/zigzag-conversion/)

---

> 2024.12.10
> 

# Approach

1. Use a list(`box`) where each index corresponds to a row in the zigzag pattern.
2. Track the current `floor` (now index) and `direction` (up or down movement).
3. Traverse the string, assigning each character to the appropriate row in `box` :
    1. If the direction needs to reverse (top or bottom now), flip the direction by multiplying it by -1.
    2. Adjust the `floor` accordingly
4. After organizing characters, iterate through `box` to construct the final string.

---

# Code

```python
from collections import deque

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Organize all chars by floor.
        box = [deque([]) for _ in range(numRows)]

        # declare variable floor & direction
        floor, direction = 0, 1

        # Iterate string and organzie chars to box
        for c in s:
            box[floor].append(c)
            if not (0 <= floor+direction < numRows):
                # U turn on Zigzag Point
                direction *= -1

            # Shift floor
            floor += direction
        
        # box to store chars to be printed.
        answerBox = deque([])

        # Iterate & Store
        for b in box:
            for c in b:
                answerBox.append(c)
        return ''.join(answerBox)
```

---

# Complexity Analysis

**Time Complexity**: O(n) → Iterate through the string once and concatenate rows.

**Space Complexity**: O(n) → Store all characters in the `box` list.

# Reflection

### Trying to optimize time complexity

This approach efficiently organizes characters into rows based on the zigzag pattern. Optimizing further might involve calculating the row positions directly without a secondary data structure (box), but the current solution balances clarity and efficiency.