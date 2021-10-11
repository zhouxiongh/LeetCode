#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 时间复杂度 o(n2) 超时
        # if len(nums) == 1:
        #     return [0]
        # re = []
        # for i, n in enumerate(nums):
        #     tmp = 0
        #     for n1 in nums[i+1:]:
        #         if n > n1:
        #             tmp += 1
        #     re.append(tmp)
        # return re
        # 时间复杂度 o(lgn)
        import bisect
        queue = []
        res = []
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]
# @lc code=end

