# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(node,greatest):
            nonlocal good
            if node == None:
                return 
            else:
                if greatest <= node.val:
                    good += 1
                greatest = max(node.val, greatest)
                dfs(node.left, greatest)
                dfs(node.right, greatest)
        dfs(root, float("-inf"))
        return good
