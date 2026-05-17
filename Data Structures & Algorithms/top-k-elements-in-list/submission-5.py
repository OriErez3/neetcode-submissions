class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        t = Counter(nums)
        for num, count in t.items():
            bucket[count].append(num)
        ret = []
        for i in range(len(bucket)-1,0,-1):
            ret.extend(bucket[i])
        if len(ret) >= k:
            return ret[:k]
