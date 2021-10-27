#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = {0}
        queue = deque()
        queue.append(rooms[0])
        while queue:
            room = queue.popleft()
            for key in room:
                if key not in keys:
                    keys.add(key)
                    queue.append(rooms[key])
        return len(keys) == len(rooms)
            

# @lc code=end

