class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        steps = []
        
        # move the largest unsorted element to back of list until sorted
        while A:
            # find max unsorted element 
            k = A.index(max(A)) + 1
            
            # if the max element is already in the right place remove it
            if k == len(A):
                A.pop()
                continue
            
            # when the max unsorted is at the front of the list we flip everything
            if k == 1:
                k = len(A)
            
            # move max unsorted to the front
            A = list(reversed(A[:k])) + A[k:]
            steps.append(k)

        return steps
