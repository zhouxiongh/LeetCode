#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def vote(nums):
            tmp = nums[0]
            count = 0
            for n in nums:
                if tmp == n:
                    count += 1
                else:
                    count -= 1
                    if count == 0: 
                        tmp = n
                        count = 1
            return tmp
        return vote(nums)
        # d = {}
        # for n in nums:
            # if n not in d:
                # d[n] = 1
            # else:
                # d[n] += 1
            # if d[n] > len(nums)//2:
                # break
        # return max(d, key=d.get)

# @lc code=end

