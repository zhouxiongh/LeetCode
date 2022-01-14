#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo_speed = 1
        hi_speed = max(piles)
        while lo_speed < hi_speed:
            m_speed = lo_speed + (hi_speed - lo_speed) // 2
            time = 0
            for pile in piles:
                time += (pile + m_speed - 1) // m_speed
            if time > h:
                lo_speed = m_speed + 1
            else:
                hi_speed = m_speed
        return lo_speed


# @lc code=end