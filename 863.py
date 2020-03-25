# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        _, result = self.distanceToTarget(root, target, K)
        return result
    
    def distanceToTarget(self, root, target, K):
        if not root:
            return None, []
        
        if root == target:
            result = []
            result += self.distanceKDescendent(target.left, 1, K)
            other = target.right
            dist = 0
        else:
            dist, result = self.distanceToTarget(root.left, target, K)
            if dist is None:
                dist, result = self.distanceToTarget(root.right, target, K)
                other = root.left
            else:
                other = root.right

            if dist is None:
                return None, result
            dist += 1

        if dist == K:
            return dist, result + [root.val]
        elif dist < K:
            return dist, result + self.distanceKDescendent(other, dist+1, K)
        else:
            return dist, result
                
    
    def distanceKDescendent(self, root, d, K):
        if not root:
            return []
        
        if d == K:
            return [root.val]
        
        result = []
        result += self.distanceKDescendent(root.left, d+1, K)
        result += self.distanceKDescendent(root.right, d+1, K)
        
        return result