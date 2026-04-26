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
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            ret.append(temp[-1].val)
        return ret
        
    
