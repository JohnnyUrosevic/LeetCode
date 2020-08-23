# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val = preorder[0]
        split = 1
        while split < len(preorder):
            if preorder[split] > val:
                break
            split += 1
        
        root = TreeNode(val)
        root.left = self.bstFromPreorder(preorder[1:split])
        root.right = self.bstFromPreorder(preorder[split:])
        return root
