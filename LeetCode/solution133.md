### [Clone Graph - LeetCode](https://leetcode.com/problems/clone-graph/)

---

> 2024.12.23
> 

# Approach

- **Summary**: Tracking all nodes, using BFS mechanism.
- **How to solve**
    - Using Dict so that anywhere and anytime, all node can be considered.
    - BFS: Track all nodes.. Queue structure should store next nodes, but it must not store a node that already has been considered.
    - When considering node, all child nodes of the node should be added to the node’s neighbors.
    - Remember the first node’s copy. and the node copied would be returned.

---

# Code

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Exception handling
        if node == None:
            return None

        # Storing all node's info
        box = {node.val: Node(node.val)}

        # Remember the first node's value
        top_val = node.val

        # Queue for BFS Tracking
        queue = deque([(node)])
        while queue:
            # Current Node
            node = queue.popleft()
            if not node:
                continue
            
            # Tracking Child nodes
            for nxt in node.neighbors:
                # Should it be tracked?
                if not nxt.val in box:
                    box[nxt.val] = Node(nxt.val)
                    queue.append(nxt)

                # Add next node to current Node
                box[node.val].neighbors.append(box[nxt.val])

        # Answer
        return box[top_val]

```

---

# Complexity Analysis

**Time Complexity**: O(n) → n nodes are considered.

**Space Complexity**: O(n) → n nodes are stored into dict. And in the graph, there are n addresses. (Each node is pointing each node)

# Review

"There was no understanding about Clone before tackling this problem. Before approaching this task, I had no clear understanding of the concept of 'cloning' in graph theory. Through studying deep copies in graphs, I've come to appreciate the importance of how each node and its edges must be replicated and assigned new memory addresses to manage them independently. This fundamental insight into safely duplicating data structures has deepened my understanding of how graph data structures operate, especially through solving this problem.”