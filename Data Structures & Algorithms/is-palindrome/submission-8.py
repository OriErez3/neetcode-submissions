class Solution:
    def isPalindrome(self, s: str) -> bool:
        nospace = s.replace(" ", "")
        compare = ""
        compare2 = ""
        for i in range(len(nospace)-1, -1, -1):
            if nospace[i].isalnum():
                compare += nospace[i]
        for i in range(len(nospace)):
            if nospace[i].isalnum():
                compare2 += nospace[i]
        print(compare)
        print(compare2)
        if compare2.lower() == compare.lower():
            return True
        else:
            return False