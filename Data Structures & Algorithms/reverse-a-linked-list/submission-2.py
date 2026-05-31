# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        before = None
        while ptr is not None:
            n = ptr.next
            ptr.next = before
            before = ptr 
            ptr = n
        return before

