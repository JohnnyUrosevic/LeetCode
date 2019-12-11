# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop, heapify
from collections import defaultdict

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        indexes = defaultdict(list)
        for i in range(len(lists)):
            if lists[i]:
                heap.append(lists[i].val)
                indexes[lists[i].val].append(i)
                lists[i] = lists[i].next
        
        heapify(heap)
        result = ListNode(0)
        curr = result
        while heap:
            val = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            
            i = indexes[val].pop()
            if lists[i]:
                heappush(heap, lists[i].val)
                indexes[lists[i].val].append(i)
                lists[i] = lists[i].next
            
        return result.next
