"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        dic = {}
        visited = set()
        if not node:
            return None
        def dfs(no):
            if no in dic:
                return dic[no]
            copy = Node(no.val)
            dic[no] = copy
            for i in no.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        return dfs(node)

