# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        stack = []
        curr = root
        
        while True:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            if not stack:
                break
            
            curr = stack.pop()
            result.append(curr.val)
            
            curr = curr.right   
            
        return result