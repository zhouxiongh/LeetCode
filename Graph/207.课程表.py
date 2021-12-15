#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

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
            # graph_[pre[1]].append(pre[0]) both works

        v = [self.State.unvisited] * numCourses

        for i in range(numCourses):
            if v[i] == self.State.unvisited:
                if dfs(i):
                    return False
        return True

# version 2
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node : int):
            """ if node has circle """
            visited[node] = -1
            for neighbour in graph_[node]:
                if visited[neighbour] == -1:
                    return True
                elif visited[neighbour] == 0:
                    if dfs(neighbour):
                        return True

            visited[node] = 1
            return False

        graph_ = [[] for i in range(numCourses)]
        for post, pre in prerequisites:
            graph_[post].append(pre)
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] != 0:
                if dfs(i):
                    return False
        return True


# @lc code=start
class Solution:
    UNVISITED = 0
    VISITED = 1
    VISITING = 2
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        def dfs(course_num):
            visited[course_num] = self.VISITING
            for n in graph[course_num]:
                if visited[n] == self.VISITED:
                    continue
                if visited[n] == self.VISITING:
                    return True
                if visited[n] == self.UNVISITED:
                    if dfs(n):
                        return True
            visited[course_num] = self.VISITED
            return False

        visited = [0] * numCourses
        graph = defaultdict(list)
        for post, pre in prerequisites:
            graph[post].append(pre)
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        return True
# @lc code=end