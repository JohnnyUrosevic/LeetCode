# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        
        stack = []

        curr = head
        while curr is not None:
            stack.append(curr)
            curr = curr.next

        size = len(stack)
        stack[size // 2].next = None
        stack = stack[size // 2+1:]

        curr = head
        while curr is not None and stack:
            add = stack.pop()

            temp = curr.next
            curr.next = add
            add.next = temp

            curr = temp
