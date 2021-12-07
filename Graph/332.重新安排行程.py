#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def visit(start):
            dests = trips[start]
            while dests:
                dest = heapq.heappop(trips[start])
                visit(dest)
            ans.append(start)

        trips = collections.defaultdict(list)
        ans = []

        for start, dest in tickets:
            trips[start].append(dest)

        for trip in trips:
            heapq.heapify(trips[trip])

        kStart = 'JFK'
        visit(kStart)
        return ans[::-1]
# @lc code=end

# version 2

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def visit(start: str):
            ends = routes[start]

            while ends:
                end = heapq.heappop(ends)
                visit(end)
            ans.append(start)

        routes = collections.defaultdict(list)
        ans = []
        for start, end in tickets:
            # routes[start].append[end]
            routes[start].append(end)

        for route in routes:
            # heapq.heapify(route)
            # heapq.heapify([route])
            heapq.heapify(routes[route])

        start_p = 'JFK'
        visit(start_p)
        return ans[::-1]

