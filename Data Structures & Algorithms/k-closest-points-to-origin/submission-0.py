class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        res = []
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            distance = ((x1**2)+(y1**2))**0.5
            heapq.heappush(h,[distance, points[i]])
        

        while(k):
            res.append(heapq.heappop(h)[1])
            k -= 1
        return res
