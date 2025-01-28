> 2025-01-28
> 

### [Combination Sum - LeetCode](https://leetcode.com/problems/combination-sum/)

---

### Approach

- Use **backtracking** to explore all combinations of candidates that sum to the target.
- Recursively add candidates to the current combination (`path`) and reduce the remaining target (`remaining`).
- Start each recursion from the current index to allow reuse of the same candidate.

---

### Code

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(remaining, start, path):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= remaining:
                    path.append(candidates[i])
                    dfs(remaining - candidates[i], i, path)
                    path.pop()

        dfs(target, 0, [])
        return result

```

---

### Complexity Analysis

- **Time Complexity**: `O(2^n)`
    - Worst-case scenario where all possible combinations of the target (`t`) are explored.
- **Space Complexity**: `O(n)`
    - Maximum recursion depth is proportional to the target value.

---

### Review

- The solution is straightforward and efficiently implements backtracking.
- The pruning step (`if candidates[i] <= remaining`) avoids unnecessary recursive calls, improving performance.
- Code is clean and well-suited for problems involving combination exploration.

---