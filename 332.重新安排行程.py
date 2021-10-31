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

        for ticket in tickets:
            trips_[ticket[0]].append(ticket[1])
        
        for trip in trips_:
            heapq.heapify(trips_[trip])
        
        kStart = 'JFK'
        visit(kStart)
        return route[::-1]
# @lc code=end

