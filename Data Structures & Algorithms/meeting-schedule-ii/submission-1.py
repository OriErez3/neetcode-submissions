"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        s,e = 0,0
        count = 0
        ret = 0
        start.sort()
        end.sort()
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
                ret = max(ret,count)
            else:  
                e += 1
                count -= 1
                ret = max(ret,count)
        return ret