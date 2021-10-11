#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(nums, l, r):
            if l + 1 >= r:
                return min(nums[l], nums[r])
            if nums[l] < nums[r]:
                return nums[l]
            mid = l + (r - l) // 2
            return min(find_min(nums, l, mid-1), find_min(nums, mid, r))
        return find_min(nums, 0, len(nums)-1)
# @lc code=end


