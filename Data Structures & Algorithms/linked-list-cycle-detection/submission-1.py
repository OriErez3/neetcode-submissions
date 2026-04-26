# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        check = True
        stack = []
        while check:
            if (ptr == None):
                return False
            if (ptr in stack):
                return True
            stack.append(ptr)
            ptr = ptr.next