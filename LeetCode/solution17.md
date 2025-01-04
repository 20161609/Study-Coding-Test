### [Letter Combinations of a Phone Number - LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

---

> 2024.12.28
> 

# Approach

1. Exception case: if the length of input string is zero, it would be returning empty list [].
2. Create Dictionary
    1. It should hash each digit with 3~4 charators. And the list should be ordered by ascending.
    2. Exception: 7, 9 should have 4 charators.
    3. string list should be stored with str format.
3. Returning
    1. All cases would be gathered. Each case should have len(digits) characters. Each charactor is selected on the list that can extract from input digits and num_dict. It uses product to gather all cases.
    2. Return List(answer): convert format (char list → str)

---

# Code

```python
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #1. Exception case: len(str)==0.
        if not digits:
            return []

        #2. Create dictionary for digits.
        num_dict = {
            2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'
        }
        
        #3. Gather all cases and create list to return.
        # - gather corresponding strings from num_dict for each digit.
        box = [num_dict[int(digit)] for digit in digits]
        
				# - create answer by joining each combination of characters produced from the product.
        answer = [''.join(x) for x in product(*box)]
        return answer
        
```

---

# Complexity Analysis

**Time Complexity**: `O(4^n)` 

- #1 → Control the exception. `O(1)`
- #2 → Constant: declaration of dict value. `O(1)`
- #3 → There’s example digits is ‘29’. Then, the box is [’abc’, ‘wxyz’]. Each case should have format including 2 charactors. It’s like ***. Each string has 3~4 charactors. So the time complexity in this example would be about 4^2. The number of charators belonged to strings can be regarded as constant, but the length of box can grow infinitely. `O(4^n)`

**Space Complexity**:

- num_dict → Constant: It’s been already determined. `O(1)`
- box →  length of digits. `O(n)`
- answer → Including all cases. It can be calculated, refering time complexity. `O(4^n)`

# Review

### Cartesian product

- It produces all possible combinations by selecting one element from each iterable.

```python
from itertools import product

list1 = ['A', 'B']
list2 = ['1', '2']

# Using the product function to create all combinations of list1 and list2
result = list(product(list1, list2))  # Result: [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

```

- The Role of the `*` (unpacking) Operator. → It allows each element in the list or tuple to be passed as separate arguments to the function.

```python
digits = "234"
num_dict = {
    '2': 'abc', '3': 'def', '4': 'ghi'
}
groups = [num_dict[digit] for digit in digits]  # ['abc', 'def', 'ghi']

# Using the * operator to pass each element of groups ...
# as individual arguments to the product function.
# Results include all combinations like ... 
# ('a', 'd', 'g'), ('a', 'd', 'h'), ..., ('c', 'f', 'i').
combinations = list(product(*groups))
```

---git 