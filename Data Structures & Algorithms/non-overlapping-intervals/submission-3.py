class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s = sorted(intervals)
        prevEnd = s[0][1]
        i = 1
        ret = 0
        while i < len(intervals):
            if prevEnd > s[i][0]:
                prevEnd = min(prevEnd, s[i][1])
                ret += 1
                i += 1
            else:
                prevEnd = s[i][1]
                i += 1
        return ret