# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1,ptr2 = l1, l2
        carry = 0
        prev = ListNode()
        ret = prev
        while ptr1 or ptr2:
            if not ptr1:
                num = ptr2.val+carry
                curr = ListNode((ptr2.val+carry)%10)
            elif not ptr2:
                num = ptr1.val+carry
                curr = ListNode((ptr1.val+carry)%10)
            else:
                num = ptr1.val+ptr2.val+carry
                curr = ListNode((ptr2.val+ptr1.val+carry)%10)
            carry = (num)//10
            prev.next = curr
            prev = curr
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        if carry != 0:
            prev.next = ListNode(carry, None)
        return ret.next 
            