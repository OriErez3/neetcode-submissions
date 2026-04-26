# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inv(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if (node == None):
                return None; 
            right = node.right
            left = node.left
            node.right = left
            node.left = right
            inv(node.left)
            inv(node.right)
            return node
        return(inv(root))
            
        