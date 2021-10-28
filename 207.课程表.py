#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(cur, v):
            if v[cur] == 1:
                return True
            if v[cur] == 2:
                return False
            
            v[cur] = 1
            for t in graph_[cur]:
                if dfs(t, v):
                    return True
            v[cur] = 2
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

