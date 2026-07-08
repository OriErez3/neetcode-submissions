class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        ret = [[] for _ in range(len(nums)+1)]
        for i in s:
            ret[s[i]].append(i)
        r = []
        t = len(nums)-1
        while len(r) != k:
            for i in ret[t]:
                r.append(i)
            t -= 1
        return r
