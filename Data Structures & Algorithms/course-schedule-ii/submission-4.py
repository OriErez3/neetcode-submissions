from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        s = defaultdict(list)
        for course,prereq in prerequisites:
            s[course].append(prereq)
        path = []
        ret = [] 
        seen = set()
        def dfs(node):
            if node in path:
                return False
            if node in seen:
                return True
            path.append(node)
            for i in s[node]:
                if not dfs(i):
                    return False
            ret.append(node)
            path.pop()
            seen.add(node)
            return True
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return ret