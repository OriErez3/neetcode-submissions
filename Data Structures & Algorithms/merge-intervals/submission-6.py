class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorts = sorted(intervals, key=lambda x : x[0])
        ret = [sorts[0]]
        if len(intervals) == 1 or len(intervals)==0:
            return intervals
        for i, e in sorts[1:]:
            if ret[-1][1] >= i:
                ret[-1][1] = max(ret[-1][1], e)
            else:
                ret.append([i,e])
        return ret

            


        