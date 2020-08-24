# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, left=root)
        row = []

        queue = deque()
        queue.append((root, 1))
        
        while queue:
            node, level = queue.popleft()
            
            if level >= d:
                break
            
            if level == d-1:
                row.append(node)
            
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        for node in row:
                node.left = TreeNode(v, left=node.left)
                node.right = TreeNode(v, right=node.right)
        return root
