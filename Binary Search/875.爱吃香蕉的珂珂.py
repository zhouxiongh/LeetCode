#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_speed = 1
        max_speed = max(piles)
        target_hours = h
        while low_speed < max_speed:
            speed = low_speed + (max_speed - low_speed) // 2
            eat_hours = 0
            for p in piles:
                eat_hours += (p + speed - 1) // speed
            if eat_hours <= target_hours:
                max_speed = speed
            else:
                low_speed = speed + 1
        return low_speed

# @lc code=end


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_speed = 1
        max_speed = max(piles)

        while low_speed < max_speed:
            guess_speed = low_speed + (max_speed - low_speed) // 2
            eat_hours = 0
            for pile in piles:
                eat_hours += (pile + guess_speed - 1) // guess_speed
            if eat_hours <= h:
                max_speed = guess_speed
            else:
                low_speed = guess_speed + 1
        return low_speed


