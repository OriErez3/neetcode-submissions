class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        ret = []
        for i in strs:
            t = [0]*26
            for l in i:
                t[ord(l)-ord("a")] += 1
            dic[tuple(t)].append(i)
        return list(dic.values())
        
