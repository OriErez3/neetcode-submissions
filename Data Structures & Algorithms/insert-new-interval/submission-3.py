class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        i = 0
        new_start = newInterval[0]
        new_end = newInterval[1]
        while i < len(intervals) and intervals[i][1] < new_start:
            start = intervals[i][0]
            end = intervals[i][1]
            ret.append([start,end])
            i += 1
        while i < len(intervals) and intervals[i][0] <= new_end:
            new_start = min(new_start,intervals[i][0])
            new_end = max(new_end,intervals[i][1])
            i += 1
        ret.append([new_start,new_end])
        while i < len(intervals):
            ret.append([intervals[i][0],intervals[i][1]])
            i += 1
        return ret
    
            
            