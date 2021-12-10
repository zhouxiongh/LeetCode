#
# @lc app=leetcode.cn id=786 lang=python3
#
# [786] 第 K 个最小的素数分数
#
from typing import List
# @lc code=start
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
# @lc code=end

