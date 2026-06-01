# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        dummy = ListNode()
        ret = dummy
        for i in range(len(lists)):
            if not lists[i]:
                continue
            h.append((lists[i].val,i,lists[i]))
        heapq.heapify(h)
        while h:
            i += 1
            t = heapq.heappop(h)
            dummy.next = t[2]
            if dummy.next.next:
                heapq.heappush(h,(dummy.next.next.val,i,dummy.next.next)) 
            dummy = dummy.next 
        return ret.next
            