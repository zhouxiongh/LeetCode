#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    # def __init__(self):
    #     self.visited = {}
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node
        visited = {}
        visited[node] = Node(node.val, [])
        queue = collections.deque([node])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbors not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # add neibor node
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]


# @lc code=start
class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        visited = {node: Node(node.val)}
        queue = deque()
        queue.append(node)
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]


# @lc code=end
