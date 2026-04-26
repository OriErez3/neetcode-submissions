class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # helper: are two trees exactly the same?
        def sameTree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        # edge case: empty subRoot is always a subtree
        if not subRoot:
            return True

        # traverse main tree and try to match subRoot at each node
        def trav(node: Optional[TreeNode]) -> bool:
            if not node:
                return False

            # if values match, check full tree equality
            if node.val == subRoot.val and sameTree(node, subRoot):
                return True

            # otherwise keep searching left or right
            return trav(node.left) or trav(node.right)

        return trav(root)