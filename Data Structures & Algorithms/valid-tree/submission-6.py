class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = [[] for i in range(n)]
        for j, l in edges:
            neighbors[j].append(l)
            neighbors[l].append(j)
        visited = set()
        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for i in neighbors[node]:
                if i == parent:
                    continue
                if not dfs(i, node):
                    return False
            
            return True 
        return dfs(0,-1) and len(visited) == n
        
                
