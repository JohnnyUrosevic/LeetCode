class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        
        i = inorder.index(preorder[0])
        
        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]
        
        left_preorder = []
        right_preorder = []
        for i in range(1,len(preorder)):
            if preorder[i] in right_inorder:
                left_preorder = preorder[1:i]
                right_preorder = preorder[i:]
                break;
        else: #no break
            left_preorder = preorder[1:]
            
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
