# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2
        ret = ListNode()
        c = ret
        while one is not None or two is not None:
            ret.next = ListNode()
            if two is None:
                ret.next.val = one.val
                ret = ret.next
                one = one.next
            elif one is None:
                ret.next.val = two.val
                ret = ret.next
                two = two.next
            elif one.val < two.val:
                ret.next.val = one.val
                ret = ret.next
                one = one.next
            else:
                ret.next.val = two.val
                ret = ret.next
                two = two.next

        return c.next