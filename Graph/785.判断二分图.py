#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
# class Solution:
#     class Color:
#         red = 1
#         blue = -1
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         def coloring(node, color):
#             """ dfs
#             return: False if conflict
#             """
#             if colors[node]:
#                 return colors[node] == color
#             colors[node] = color
#             for n in graph[node]:
#                 if not coloring(n, -color):
#                     return False
#             return True
#         n = len(graph)
#         colors = [None] * n
#         for i in range(n):
#             if not colors[i]:
#                 if not coloring(i, self.Color.red):
#                     return False
#         return True
class Solution:
    # class Color:
    red = 1
    green = -1

    def isBipartite(self, graph: List[List[int]]) -> bool:
        def coloring(node, color):
            if colors[node]:
                return colors[node] == color
            colors[node] = color
            for neighbor in graph[node]:
                if coloring(neighbor, -color) == False:
                    return False
            return True
        n = len(graph)
        colors = [None] * n
        for i in range(n):
            if colors[i] is None:
                if coloring(i, self.red) == False:
                    return False
        return True


# @lc code=end

