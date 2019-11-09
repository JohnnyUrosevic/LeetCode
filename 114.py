class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, l):
        if root is None:
            return l
        
        l.append(TreeNode(root.val))
        l = self.helper(root.left, l)
        l = self.helper(root.right, l)

        return l

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        l = self.helper(root, [])
        
        root.left = None
        node = root
        for n in l[1:]:
            node.right = n
            node = node.right
        root = root.right

        
if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    sol = Solution()
    sol.flatten(root)
    while root is not None:
        print(root.val)
        root = root.right
