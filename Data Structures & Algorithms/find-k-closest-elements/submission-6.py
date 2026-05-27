class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, len(arr)-k
        m = r//2
        while l<r:
            if x-arr[m]>arr[m+k]-x:
                l = m+1
            else:
                r = m
            m = (l+r)//2
        return arr[l:l+k]