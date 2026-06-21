import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i,n in enumerate(nums):
            heap.append([n,i])
        heapq.heapify(heap)
        for i in range(k):
            temp = heapq.heappop(heap)
            temp[0] = temp[0]*multiplier
            nums[temp[1]] = temp[0]
            heapq.heappush(heap,temp)
        return nums