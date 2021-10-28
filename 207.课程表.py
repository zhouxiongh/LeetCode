#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    class State:
        unkonwn = 0
        visiting = 1
        visited = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(cur, v):
            """
            cur: current course index
            v: states: 0 = unkonwn, 1 == visiting, 2 = visited
            """
            if v[cur] == self.State.visiting:
                return True
            if v[cur] == self.State.visited:
                return False
            
            v[cur] = self.State.visiting
            for t in graph_[cur]:
                if dfs(t, v):
                    return True
            v[cur] = self.State.visited
            return False

        graph_ = [[] for j in range(numCourses)]

        for pre in prerequisites:
            graph_[pre[0]].append(pre[1])
        
        v = [0] * numCourses

        for i in range(numCourses):
            if dfs(i, v):
                return False
        return True
# @lc code=end

