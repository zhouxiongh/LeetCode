#
# @lc app=leetcode.cn id=786 lang=python3
#
# [786] 第 K 个最小的素数分数
#
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        frac_arr = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        heapq.heapify(frac_arr)
        i = 0
        while i < k-1:
            i += 1
            frac = heapq.heappop(frac_arr)
            idx, idy = frac.idx, frac.idy
            if idx + 1 < idy:
                heapq.heappush(frac_arr, Frac(idx+1, idy, arr[idx+1], arr[idy]))
        return frac_arr[0].x, frac_arr[0].y

class Frac:
    def __init__(self, idx, idy, x, y):
        self.idx, self.idy = idx, idy
        self.x, self.y = x, y
    def __lt__(self, other):
        return self.x * other.y < self.y * other.x

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        def cmp(item1, item2):
            return 1 if item1[0] * item2[1] > item1[1] * item2[0] else -1
        n = len(arr)
        new_arr = list()
        for i in range(n):
            for j in range(i+1, n):
                new_arr.append((arr[i], arr[j]))
        new_arr.sort(key=cmp_to_key(cmp))
        return new_arr[k-1]

# @lc code=start
class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        new_arr = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        heapq.heapify(new_arr)
        i = 0
        while i < k -1:
            i += 1
            frac = heapq.heappop(new_arr)
            if frac.idx + 1 < frac.idy:
                heapq.heappush(new_arr, Frac(frac.idx+1, frac.idy, arr[frac.idx+1], arr[frac.idy]))
        return new_arr[0].x, new_arr[0].y


class Frac:
    def __init__(self, idx, idy, x, y):
        self.idx = idx
        self.idy = idy
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x * other.y < self.y * other.x
# @lc code=end