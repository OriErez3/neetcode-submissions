class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1]*n
        def find(n):
            while parent[n] != n:
                n = parent[n]
            return n
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra,rb = rb,ra
            parent[rb] = ra
            rank[ra] += rank[rb] 
            return True
        components = n
        for a,b in edges:
            if union(a,b):
                components -= 1
        return components
        