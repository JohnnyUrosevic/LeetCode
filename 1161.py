# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [(root, 0)]
        levels = []

        while queue:
            node, level = queue.pop()

            if level == len(levels):
                levels.append(0)

            levels[level] += node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            

        return levels.index(max(levels)) + 1
