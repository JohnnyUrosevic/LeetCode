# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        return self.helper(root, [], s)
    
    def helper(self, root, path, s):
        if not root:
            return []
        
        path.append(root.val)
        if not root.left and not root.right and sum(path) == s:
            return [path]
        
        old_path = path.copy()
        result = []
        
        left = self.helper(root.left, path, s)
        path = old_path
            
        right = self.helper(root.right, path, s)
        
        if left:
            result += left
        if right:
            result += right
            
        return result
