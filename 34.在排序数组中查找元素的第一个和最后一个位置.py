#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_pos(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r-l) // 2
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            if l == len(nums) or nums[l] != target:
                return -1
            return l
                
        def second_pos(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r-l) // 2
                if target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            l -= 1
            if l < 0 or nums[l] != target:
                return -1
            return l
        return [first_pos(nums, target), second_pos(nums, target)]
        
# @lc code=end

