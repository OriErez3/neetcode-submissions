import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0, k-1
        ret = []
        n = {-x:i for i, x in enumerate(nums)}
        h = [(-nums[i], i) for i in range(r+1)]
        heapq.heapify(h)
        while r < len(nums):
            heapq.heappush(h, (-nums[r],r))
            while h[0][1] < l:
                heapq.heappop(h)
            ret.append(-h[0][0])
            l += 1
            r += 1
        return ret

            



        