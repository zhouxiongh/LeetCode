#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # def mergeSort(nums, l, r):
        #     if l + 1 > r:
        #         return
        #     m = l + (r - l) // 2
        #     mergeSort(nums, l, m)
        #     mergeSort(nums, m, r)
        #     pass
        # mergeSort(nums, 0, len(nums))
        # return nums
        list.sort(nums)
        return nums
# @lc code=end

