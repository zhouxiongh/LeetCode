#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def visit(start):
            dests = trips_[start]
            while dests:
                dest = heapq.heappop(trips_[start])
                visit(dest)
            route.append(start)

        trips_ = collections.defaultdict(list)
        route = []

        for start, end in tickets:
            trips_[start].append(end)
        
        for trip in trips_:
            heapq.heapify(trips_[trip])
        
        kStart = 'JFK'
        visit(kStart)
        return route[::-1]
# @lc code=end

