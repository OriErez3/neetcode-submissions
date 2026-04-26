# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        dummy = ListNode(0, head)
        ptr2 = dummy
        for i in range(n):
            ptr = ptr.next
        while (ptr != None):
            ptr = ptr.next
            ptr2 = ptr2.next
        ptr2.next= ptr2.next.next
        return dummy.next
