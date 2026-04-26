"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorts = sorted(intervals, key=lambda x: x.start)      
        for i in range(len(sorts)-1):
            if (sorts[i].end > sorts[i+1].start):
                return False
        return True