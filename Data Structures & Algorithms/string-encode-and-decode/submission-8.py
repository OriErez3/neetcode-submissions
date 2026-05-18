class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            ret += str(len(i))
            ret += "#"
            ret += i
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i != len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            ret.append(s[j+1:length+j+1])
            i = length+j+1
        return ret 