from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        s = defaultdict(list)
        for i, j in edges:
            s[i].append(j)
            s[j].append(i)
        visited = set()
        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for checks in s[node]:
                if checks == parent:
                    continue
                if not dfs(checks,node):
                    return False
            return True
        return (dfs(0,-1) and len(visited) == n)