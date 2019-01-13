# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        q = Queue()
        q.put(root)
        
        numInRow = 1
        count = 0;
        
        maxVal = None
        
        result = []
        
        while not q.empty():
            node = q.get();
            count += 1
            
            if node is None:
                q.put(None)
                q.put(None)  
            elif maxVal is None:
                maxVal = node.val
            elif node.val > maxVal:
                maxVal = node.val
                
            if count == numInRow:
                if (maxVal is None):
                    return result
                result.append(maxVal)
                maxVal = None 
                numInRow *= 2
                count = 0
            
            if node is not None:
                q.put(node.left)
                q.put(node.right)
            
        return result
            
