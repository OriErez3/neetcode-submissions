class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals)
        ret = []
        i=0 
        while i < len(intervals):
            start = s[i][0]
            end = s[i][1]
            if ret and start<=ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], end)
            else:
                ret.append([start,end])
            i += 1
        return ret

            


        