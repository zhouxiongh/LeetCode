#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class MyLinkedList:

    def __init__(self):
        self._val = []

    def get(self, index: int) -> int:
        if index not in range(len(self._val)):
            return -1
        return self._val[index]

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self._val.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if len(self._val) == 0 or index not in range(len(self._val)):
            self._val.append(val)
            return
        last_index = len(self._val) - 1
        self._val.append(self._val[last_index])
        while index < last_index:
            self._val[last_index] = self._val[last_index-1]
            last_index -= 1
        self._val[index] = val


    def deleteAtIndex(self, index: int) -> None:
        if index not in range(len(self._val)):
            return
        while index < len(self._val) - 1:
            self._val[index] = self._val[index+1]
            index += 1
        self._val.pop()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(2)
# obj.deleteAtIndex(1)
# obj.addAtHead(2)
# obj.addAtHead(7)
# obj.addAtHead(3)
# obj.addAtHead(2)
# obj.addAtHead(5)
# obj.addAtTail(5)
# print(obj.get(5))
# obj.deleteAtIndex(6)
# obj.deleteAtIndex(4)
# @lc code=end

