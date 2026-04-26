# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []
        if root==None:
            return []
        while queue:
            temp = []
            level_size = len(queue)
            for i in range(level_size):
                t = queue.popleft()
                if t.left != None:
                    queue.append(t.left)
                if t.right != None:
                    queue.append(t.right)
                temp.append(t.val)
            ans.append(temp)
        return ans
            
