class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()
        adj = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            adj[i].append(j)
        def dfs(node):
            nonlocal visited
            nonlocal path
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            for i in adj[node]:
                if not dfs(i):
                    return False
            path.remove(node)
            visited.add(node)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
    

                    
            
            