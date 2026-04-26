class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        total = set()
        def find(n):
            if parents[n] == n:
                return n
            else:
                return find(parents[n])
        def union(a,b):
            parents[find(a)] = find(b)
        for i,j in edges:
            union(i,j)
        for l in parents:
            total.add(find(l))
        return len(total)