#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def valid_mutation(s1, s2):
            count = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    count += 1
                if count > 1:
                    return False
            return True

        queue = collections.deque()
        queue.append(start)
        visited = set()
        ans = 0

        while queue:
            size = len(queue)
            while size:
                size -= 1
                cur  = queue.popleft()
                if cur == end:
                    return ans
                for b in bank:
                    if valid_mutation(cur, b) and b not in visited:
                        queue.append(b)
                        visited.add(b)
            ans += 1
        return ans
        
            
# @lc code=start
class Solution:
    def minMutation(self, start, end, bank):
        def valid_mutation(cur, mutate):
            counter = 0
            for c1, c2 in zip(cur, mutate):
                if c1 != c2:
                    counter += 1
            return counter == 1
        queue = deque()
        queue.append(start)
        visited = set()
        ans = 0
        while queue:
            size = len(queue)
            while size:
                size -= 1
                cur = queue.popleft()
                if cur == end:
                    return ans
                for gene in bank:
                    if valid_mutation(cur, gene) and gene not in visited:
                        queue.append(gene)
                        visited.add(gene)
            ans += 1
        return -1

# @lc code=end