class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(list(filter(lambda st: len(st) > 0, s.split(" "))))
