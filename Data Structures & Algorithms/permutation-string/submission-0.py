from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original = Counter(s1)
        gap = len(s1)
        for lp in range(len(s2)):
            rp = lp+gap
            potential_string = s2[lp:rp]
            checkString = Counter(potential_string)
            if checkString == original:
                return True
        return False

        