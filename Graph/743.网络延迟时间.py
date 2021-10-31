#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX_TIME = 101 * 100
        dist = [MAX_TIME] * (n+1)
        dist[k] = 0 # start form k
        for i in range(1, n+1):
            for time in times:
                u, v, w = time[0] ,time[1], time[2]
                dist[v] = min(dist[v], dist[u] + w)
        max_dist = max(dist[1:])
        return -1 if max_dist == MAX_TIME else max_dist

# @lc code=end

