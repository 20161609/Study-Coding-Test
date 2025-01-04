> 2025.01.04
> 

### [Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

---

# Approach

- Sliding Window Technique: The problem is solved using a **Sliding Window** approach to dynamically adjust the substring’s start (`left`)  and end (`right`) indices while iterating through the string.
    - Maintain a directory `recent_index` to track the most index of each character.
    - If a character repeats within the current window, update the left pointer to execute the repeated character.
    - Continuously calculate the length of the valid substring and update the answer.

---

# Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, n = 0, len(s)

        # Updated when a longer one is found
        answer = 0

        # It stores the most recent index of the given character.
        recent_index = {} 

        # Iterating through the string s
        for right in range(len(s)):
            char = s[right]
            if (char in recent_index) and left <= recent_index[char]:
                # Next left index should be 'recent index of char' + 1
                left = recent_index[char] + 1
            else:
                # Substring(s[left:right+1]) is valid..
                # Calculate length substring and update answer
                answer = max(right-left+1, answer)

            # Update recent Index
            recent_index[char] = right

        return answer
```

---

# Complexity Analysis

**Time Complexity**: `O(n)` 

- Each character in the string is visited at most twice, once for expanding the `right` pointer possibly once for adjusting the `left` pointers.

**Space Complexity**: `O(n)` 

- The `recent_index` dictionary stores the indices of characters, and its size is limited by the number of unique characters in the string.

# Review

- The code effectively uses the sliding window technique to achieve optimal performance with O(n) time complexity.
- Using hash map (recent_index) helps the solution easily to track most recent indices, making it well-suited for this type of problem.

---