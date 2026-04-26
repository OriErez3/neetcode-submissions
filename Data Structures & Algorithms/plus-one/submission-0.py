class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        track = ""
        ret = []
        for i in digits:
            track += str(i)
        track = int(track)+1
        for i in str(track):
            ret.append(int(i))
        return ret
            
        