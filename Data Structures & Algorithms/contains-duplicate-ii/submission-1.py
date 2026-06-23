from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        f = defaultdict(list)
        ret = False
        for i, n in enumerate(nums):
            if n in f:
                ret = (abs(i-max(f[n]))<=k)
            f[n].append(i)
        return ret
        