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
        if root == None:
            return []
        while queue:
            level_size = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i == level_size-1:
                    ret.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
        return ret
        
    
