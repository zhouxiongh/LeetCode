#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_num = list(bin(n))
        # skip 0b
        for i in range(2, len(bin_num)):
            if bin_num[i] == '0':
                bin_num[i] = '1'
            else:
                bin_num[i] = '0'

        return int(''.join(bin_num), 2)
# @lc code=end

