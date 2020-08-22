# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import SimpleQueue
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = SimpleQueue()
        queue.put((root, 0))
        
        right = []
        while not queue.empty():
            node, level = queue.get()
            
            if level == len(right):
                right.append(0)
            
            right[level] = node.val
            
            if node.left:
                queue.put((node.left, level+1))
            if node.right:
                queue.put((node.right, level+1))
        
        return right
