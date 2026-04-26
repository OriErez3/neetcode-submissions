class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        def find(node):
            if parent[node] == node:
                return node
            else:
                return find(parent[node])
        def union(a,b):
            if find(a) == find(b):
                return [a,b]
            else:
                parent[find(a)] = find(b)
        for i,j in edges:
            if union(i,j):
                return union(i,j)