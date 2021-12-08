#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_pos(nums, target):
            l = 0 # 单调递增
            r = len(nums) # 单调递减
            while l < r:
                mid = l + (r-l) // 2
                # 等于或小于搜索范围向右逼近，找到第一个位置
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            # 结束循环 nums[mid] > target
            # mid + 1 即第一个位置
            if l == len(nums) or nums[l] != target:
                return -1
            return l

        def last_pos(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r-l) // 2
                if target < nums[mid]:
                    r = mid
                # 大于或等于搜索范围向左逼近，找到最后一个位置
                else:
                    l = mid + 1
            # 结束循环时 nums[mid] >= target
            # mid + 1 是第一个大于且不等于target的位置
            l -= 1
            if l < 0 or nums[l] != target:
                return -1
            return l
        return [first_pos(nums, target), last_pos(nums, target)]

# @lc code=end

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_pos(nums, target):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = lo + (hi-lo) // 2
                if nums[mid] >= target:
                    hi = mid - 1
                else:
                    lo = mid
            hi += 1
            if hi == len(nums) or nums[hi] != target:
                return -1
            return hi
        def last_pos(nums, target):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = lo + (hi-lo) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            lo -= 1
            if lo < 0 or nums[lo] != target:
                return -1
            return lo
        return [first_pos(nums, target), last_pos(nums, target)]
