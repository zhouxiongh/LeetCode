#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s = UnionFindSet(len(edges))
        for edge in edges:
            if not s.union(edge[0], edge[1]):
                return edge
        return None

class UnionFindSet:
    def __init__(self, n):
        # start from 0
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for i in range(n + 1)]
    
    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def union(self, u, v):
        """
        return: bool
        False if u, v already union
        """
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:        
            self._parents[pv] = pu
            self._ranks[pu] += 1
        
        return True

# second
class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(1, n+1)]
        self._ranks = [1 for i in range(1, n+1)]

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
        # pu, pv = self._parents[u], self._parents[v]
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        elif self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        else:
            self._parents[pu] = pv
            self._ranks[pv] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFindSet(n)
        for edge in edges:
            if uf.union(edge[0], edge[1]) == False:
                return edge
        return None

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        uf = UnionFindSet(n)
        # build union find set
        for edge in edges:
            if uf.union(edge[0], edge[1]):
                return edge
        return None
class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n+1)]
        self._ranks = [1] * (n+1)

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return True
        if self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
            self._ranks[pu] += self._ranks[pv]
        else:
            self._parents[pu] = pv
            self._ranks[pv] += self._ranks[pu]
        return False

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

# @lc code=end