class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for n in s:
            c = s[n]
            bucket[c].append(n)
        ret = []
        for c in range(len(bucket) - 1, 0, -1):
            for n in bucket[c]:
                ret.append(n)
                if len(ret) == k:
                    return ret
        
            
