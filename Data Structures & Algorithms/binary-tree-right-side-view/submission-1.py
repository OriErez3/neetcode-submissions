# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        queue = deque([root])
        ans = []
        if root == None:
            return []
        while queue:
            level_len = len(queue)
            t = []
            for i in range(level_len):
                temp = queue.popleft()
                t.append(temp)
                if temp.left != None: queue.append(temp.left)
                if temp.right != None: queue.append(temp.right)
            ans.append(t[len(t)-1].val)
        return ans
            
        