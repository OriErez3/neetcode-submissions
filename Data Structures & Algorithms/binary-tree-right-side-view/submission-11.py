# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ret = []
        queue = deque()
        queue.append(root)
        while queue:
            if queue[-1]:
                ret.append(queue[-1].val)
            length = len(queue)
            for i in range(length):
                t = queue.popleft()
                if t and t.left:
                    queue.append(t.left)
                if t and t.right:
                    queue.append(t.right)
        return ret
