# LeetCode #6. Zigzag Conversion
# 24.12.10
# https://leetcode.com/problems/zigzag-conversion/description/

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
    