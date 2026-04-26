# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def preOrder(dfs):
            if not dfs:
                return; 
            preOrder(dfs.left)
            arr.append(dfs.val)
            preOrder(dfs.right)
        preOrder(root)
        return arr[k-1]