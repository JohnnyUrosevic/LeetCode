# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        
        root = TreeNode(pre[0])
        
        if (len(pre) == 1):
            return root
        
        i = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1:i], post[:i-1])
        root.right = self.constructFromPrePost(pre[i:], post[i-1:-1])
        
        return root