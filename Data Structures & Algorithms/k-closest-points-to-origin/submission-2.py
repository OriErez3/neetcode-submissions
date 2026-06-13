import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ret = []
        distances = []
        for x,y in points:
            dist = (math.sqrt(x*x+y*y)) 
            distances.append((dist,[x,y]))
        heapq.heapify(distances)
        for i in range(k):
            t = heapq.heappop(distances)
            ret.append(t[1])
        return ret
        