class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            path[crs].append(pre)
        
        Vset = set()
        def dfs(crs):
            if crs in Vset:
                return False
            if path[crs] == []:
                return True
            Vset.add(crs)
            for pre in path[crs]:
                if not dfs(pre): return False
            Vset.remove(crs)
            path[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

            
            