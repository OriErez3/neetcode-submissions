"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        seen = {}
        if node == None:
            return None
        def dfs(n):
            if n in seen:
                return seen[n]
            else:
                t = Node(n.val, [])
                seen[n] = t
                t.neighbors = [dfs(neighbor) for neighbor in n.neighbors]
                return seen[n]
                
        dfs(node)
        return seen[node]

