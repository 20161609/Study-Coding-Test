> 2024.12.28
> 

### [Valid Parentheses - LeetCode](https://leetcode.com/problems/valid-parentheses/)

---

# Approach

- opening(list) → to figure out if the charactor is openning sign.
- closing_dict → to figure out if the closing sign matches the stack’s last node.
- Scanning Iterating str and consider each charactor c
    - If c is openning sign, the charactor should be pushed into stack.
    - The c is closing sign, check if the charactor matches stack’s top. If it is true, stack should pop, but if it is false, it returns false.
    - when c is closing sign but the stack is empty, it must return false too.
- Return answer → if the stack is empty

---

# Code

```python
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Basic informations about closing and openning
        opening = ['(', '{', '[']
        closing_dict = {')':'(', '}':'{', ']':'['}

        # 2. Scanning the str. And 
        stack = deque([])
        for c in s:
            if c in opening:
                stack.append(c)
            elif stack and (stack[-1] == closing_dict[c]):
                stack.pop()
            else:
                return False
        
        # 3. Return answer(The stack must be empty)
        return not stack
```

---

# Complexity Analysis

**Time Complexity**: O(n) → Iterating str. And the time complexity considering each character would be O(1).

**Space Complexity**: O(n) → stack structure can have up to length of str things.

# Review

Using stack was important thing. Stack structure can make it to easily get most recently added member.