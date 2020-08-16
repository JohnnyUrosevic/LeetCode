class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sorter(item):
            count = 0
            temp = item
            while temp:
                count += temp % 2
                temp //= 2
                
            return (count,item)
        
        return sorted(arr, key=sorter)
