"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        h = { None : None }
        while ptr:
            h[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            copy = h[ptr]
            copy.next = h[ptr.next]
            copy.random = h[ptr.random]
            ptr = ptr.next
        
        return h[head]

