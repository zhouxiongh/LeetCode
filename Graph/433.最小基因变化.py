#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
from typing import List
import collections
# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """ shortest path """
        def validMutation(s1, s2):
            count = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    count += 1
                    if count > 1:
                        return False
            return True
        ans = 0
        queue = collections.deque()
        queue.append(start)
        visited = set()
        while queue:
            size = len(queue)
            while size:
                size -= 1
                s = queue.popleft()
                if s == end:
                    return ans
                for b in bank:
                    if b not in visited and validMutation(s, b):
                        visited.add(b)
                        queue.append(b)
            ans += 1
        return -1
                    
        
# @lc code=end
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(Solution().minMutation(start, end, bank))
