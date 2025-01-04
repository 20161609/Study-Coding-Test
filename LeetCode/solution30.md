> 2024.12.31
> 

### [Substring with Concatenation of All Words - LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

---

# Approach

- Calculate frequency of words:
    - There can be duplication of words.
    - Use a dictionary to track the frequency.
- Create list box:
    - Store words from string `s` that match words in frequency dictionary.
    - All of words have same size.
- Gather indexes that satisfy concatenation condition:
    - Use frequency dictionary. If it is satisfying, the dict would be empty.
    - Iterate over the substring and check if it meets condition.

---

# Code

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Init variable
        word_size = len(words[0]) # length of word
        substring_size = word_size * len(words) # number of words

        # Calculate the frequency 
        frequency = {}
        for word in words:
            if word not in frequency:
                frequency[word] = 0
            frequency[word] += 1

        # Store words that match to index in string s.
        box = [None] * len(s)
        for i in range(0, len(s) - word_size + 1):
            if s[i:i+word_size] in frequency:
                box[i] = s[i:i+word_size]
        
        # Consider substring and figure out if it is satisfying.
        answer = []
        for i in range(len(s) - substring_size + 1):
            # temporary dict to figure out if it is concatenation.
            temp = {word: frequency[word] for word in frequency}

            # iterating over a substring of string s.
            for j in range(i, i + substring_size, word_size):
                if box[j] is None or box[j] not in temp:
                    break

                # if it is included..
                temp[box[j]] -= 1
                if temp[box[j]] == 0:
                    temp.pop(box[j])

            # check if it is concatenation.
            if not temp:
                answer.append(i)
                
        return answer

```

---

# Complexity Analysis

> Let n be size of list words.
> 

**Time Complexity**: `O(n)` 

- The maximum size of word is 30. So, the time complexity would be considered with iterating string s.

**Space Complexity**: `O(n)` 

- `frequency`  It grows with the number of distinct words.
- `box` There are n members. Each case has word or Null. The word’s size is limited. O(30*n)

# Review

It was challenging to minimize time complexity. Employing a hashing technique significantly aided this effort by allowing efficient lookups and updates.