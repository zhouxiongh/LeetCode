#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from typing import List
import collections
# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         def divide(x, y, visited):
#             """ dfs
#             x / y = divide(x, n) * divide(n, y)
#             """
#             if x == y:
#                 return 1.0
#             visited.add(x)
#             for n in graph_[x]:
#                 if n in visited:
#                     continue
#                 visited.add(n)
#                 ndy = divide(n, y, visited)
#                 if ndy > 0:
#                     return ndy * graph_[x][n]
#             return -1.0
#         ans = []
#         graph_ = collections.defaultdict(dict)
#         for (x, y), v in zip(equations, values):
#             graph_[x][y] = v
#             graph_[y][x] = 1.0 / v
#         for x, y in queries:
#             if x in graph_ and y in graph_:
#                 ans.append(divide(x, y, set()))
#             else:
#                 ans.append(-1.0)
#         return ans
class Solution:
    def calcEquation(self, equations, values, queries):
        def divide(x, y, visited):
            # x / y = x / n * n / y
            if x == y:
                return 1.0
            visited.add(x)
            for n in graph[x]:
                if n in visited:
                    continue
                visited.add(n)
                ndy = divide(n, y, visited)
                if ndy > 0:
                    return ndy * graph[x][n]
            return -1.0

        graph = defaultdict(dict)
        ans = []
        for (x, y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1.0 / value
        for query in queries:
            if query[0] in graph and query[1] in graph:
                ans.append(divide(query[0], query[1], set()))
            else:
                ans.append(-1.0)

        
        return ans

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
ans = Solution().calcEquation(equations, values, queries)
print(ans)

# @lc code=start
class Solution:
    def calcEquation(self, equations, values, queries):
        def divide(x, y, visited):
            if x == y:
                return 1.0
            # x / y = x / n * n / y
            visited.add(x)
            for n in graph[x]:
                if n in visited:
                    continue
                ndy = divide(n, y, visited)
                if ndy > 0:
                    return graph[x][n] * ndy
            return -1.0
        graph = defaultdict(dict)

        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1.0 / v
        
        ans = list()
        for x, y in queries:
            if x in graph and y in graph:
                ans.append(divide(x, y, set()))
            else:
                ans.append(-1.0)
        return ans


# @lc code=end