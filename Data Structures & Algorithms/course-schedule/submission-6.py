from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        s = defaultdict(list)
        for i,j in prerequisites:
            s[i].append(j)
        visited = set()
        current_path = set()
        def dfs(node):
            if node in current_path:
                return False
            if node in visited:
                return True
            current_path.add(node)
            for i in s[node]:
                if dfs(i) == False:
                    return False
            current_path.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
            