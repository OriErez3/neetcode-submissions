class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        m = {}
        for i in hand:
            m[i] = 1 + m.get(i,0)
        minH = list(m.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]          

            for i in range(first, first+groupSize):
                if i not in m:
                    return False      
                m[i] -= 1
                if m[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True