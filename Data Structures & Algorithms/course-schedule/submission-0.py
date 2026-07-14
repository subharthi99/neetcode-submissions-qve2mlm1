class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if adjMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in adjMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            adjMap[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True