class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        t = [[] for i in range(len(nums)+1)]
        for num, freq in s.items():
            t[freq].append(num)
        ret = []
        for r in range(len(t)-1,0,-1):
            for num in t[r]:
                ret.append(num)
                if len(ret) == k:
                    return ret

