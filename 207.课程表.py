#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    class State:
        unvisited = 0
        visiting = 1 # 临时标记
        visited = 2 # 永久标记

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(cur):
            """
            拓扑排序: O(n)
            cur: current course index
            v: states: 0 = unkonwn, 1 == visiting, 2 = visited
            return: True 有环, False 无环
            """
            v[cur] = self.State.visiting
            for neighbour in graph_[cur]:
                if v[neighbour] == self.State.visiting:
                    return True
                elif v[neighbour] == self.State.unvisited:
                    if dfs(neighbour):
                        return True
            v[cur] = self.State.visited
            # add cur node to topo node if needed
            return False
        
        graph_ = [[] for j in range(numCourses)]

        for pre in prerequisites:
            graph_[pre[0]].append(pre[1])
        
        v = [self.State.unvisited] * numCourses

        for i in range(numCourses):
            if v[i] == self.State.unvisited:
                if dfs(i):
                    return False
        return True
# @lc code=end

