class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        if s == goal:
            if len(set(s)) != len(goal):
                return True
            return False
        n = len(s)
        i = 0
        diff = []
        _s = []
        _goal = []
        while i < n:
            if s[i] != goal[i]:
                diff.append(i)
            _s.append(s[i])
            _goal.append(goal[i])
            i += 1
        if len(diff) != 2:
            return False
        tmp = s[diff[0]]
        _s[diff[0]] = s[diff[1]]
        _s[diff[1]] = tmp
        return _s == _goal