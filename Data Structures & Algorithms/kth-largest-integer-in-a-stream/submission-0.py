import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = [-i for i in nums]
        heapq.heapify(self.h)
        self.number = k

    def add(self, val: int) -> int:
        heapq.heappush(self.h,-val)
        arr = []
        for i in range(self.number):
            arr.append(heapq.heappop(self.h))
        ret = arr[-1]
        for i in arr:
            heapq.heappush(self.h,i)
        return -ret
            
