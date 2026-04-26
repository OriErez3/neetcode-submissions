class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        track = n
        while track != 1:
            if track in check:
                return False 
            check.add(track)
            track2 = 0 
            for i in str(track):
                d = int(i)
                track2 += d*d
            track = track2
        return True
            

        



        
                
        