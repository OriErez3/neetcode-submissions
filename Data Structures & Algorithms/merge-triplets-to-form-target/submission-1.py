class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                triplets.remove(i)
        c1,c2,c3 = False,False,False
        for i in triplets:
            if i[0] == target[0]:
                c1 = True
            if i[1] == target[1]:
                c2 = True
            if i[2] == target[2]:
                c3 = True
        return c1 and c2 and c3