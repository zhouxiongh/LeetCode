#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_str2int(timePoints):
            times = []
            for time in timePoints:
                hour = int(time[:2])
                minute = int(time[3:])
                times.append(hour * 60 + minute)
            return times
        ans = float('inf')
        times = time_str2int(timePoints)
        times.sort()
        for i in range(1, len(times)):
            diff = min(times[i] - times[i-1], times[i-1] + 1440 - times[i])
            if diff < ans:
                ans = diff
        ans = min(ans, times[0] + 1440 - times[-1])
        return ans


# @lc code=end

