class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        check = Counter(s1)
        c = Counter(s2[0:len(s1)])
        if c == check:
                return True
        for i in range(len(s2)-len(s1)):
            r = i+len(s1)
            c[s2[r]] = 1 + c.get(s2[r],0)
            
            c[s2[i]] = c.get(s2[i],1)-1
            if c[s2[i]] == 0: del c[s2[i]]
            if c == check:
                return True
        return False