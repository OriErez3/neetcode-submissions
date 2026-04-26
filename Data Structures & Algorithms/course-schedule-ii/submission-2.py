class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbors = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            neighbors[i].append(j)
        path = set()
        visited = set()
        vist = []
        def dfs(node):
            nonlocal visited
            nonlocal path
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            for i in neighbors[node]:
                if not dfs(i):
                    return False
            path.remove(node)
            visited.add(node)
            vist.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return vist
