class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for i in strs:
            freq = [0]*26
            for char in i:
                freq[ord(char) - ord('a')] += 1
            counts[tuple(freq)].append(i)
        ret = []
        for i in counts:
            t = counts[i]
            ret.append(t)
        return list(counts.values())
        

        
