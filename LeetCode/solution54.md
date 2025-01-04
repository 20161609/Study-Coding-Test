> 2025.01.05
> 

### [Spiral Matrix - LeetCode](https://leetcode.com/problems/spiral-matrix/description/)

---

# Approach

- The problem requires traversing a 2D matrix in a spiral order.
- Initialize directional movements for right, down, left, and up.
- Use a pointer `d` to keep track of the current direction.
- Iterate through all elements of the matrix while appending values to the result list.
- Update the direction when reaching a boundary or a previously visited cell.
- Return the resulting list.

---

# Code

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Number of rows, cols
        height, width = len(matrix), len(matrix[0])

        # Directions for traversal (right->down->left->up)
        directions, d = [[+1, 0], [0, +1], [-1, 0], [0, -1]], 0

        # List to return: nums in matrix will be collected in a sprial order.
        answer = []

        # Iterate through matrix in a sprial order.
        x, y = 0, 0
        for _ in range(width * height):
            # Append the current value into answer list
            answer.append(matrix[y][x])
            matrix[y][x] = None # Mark the cell as visited.

            # Calculate the next coordination (x,y)
            dx, dy = directions[d]
            if not(0<=x+dx<width and 0<=y+dy<height) or (matrix[y+dy][x+dx] == None):
                # The direction should be modified.
                d = (d+1)%4
                dx, dy = directions[d]
            x, y = x + dx, y + dy

        return answer

```

---

# Complexity Analysis

**Time Complexity**: `O(m*n)` 

- The matrix contains `m * n` elements, and we visit each element exactly once.

**Space Complexity**: `O(1)` 

- The space used by the algorithm is constant, excluding the output list. The `answer` list holds all `m * n` elements, which is necessary for the result and not additional overhead.

# Review

The solution is efficient for its purpose, using constant auxiliary space aside from the output list. The use of a directional matrix simplifies the logic for changing directions and ensures all cells are visited exactly once. The approach is clean, and the handling of boundary conditions is straightforward. Great for solving the problem within the constraints.