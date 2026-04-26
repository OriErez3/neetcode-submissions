class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        invnums = [-i for i in nums]
        heapq.heapify(invnums)
        for i in range(k-1):
            heapq.heappop(invnums)

        return invnums[0]*-1