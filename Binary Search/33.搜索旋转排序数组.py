#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if target == nums[mid]:
                return mid
            # 0 ... mid 有序
            # mid 可能等于0
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # mid ... end 有序
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1




class Solution(object):
    """docstring for Solution"""
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] == target:
                return mid
            # lo ... mid sorted
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # mid ... end sorted
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

# @lc code=start
class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
# @lc code=end