class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        check = list(zip(position,speed))
        stack = []
        for i in sorted(check, reverse=True):
            stack.append(i)
            if len(stack) >= 2:
                time1 = (target-stack[-1][0])/stack[-1][1]
                time2 = (target-stack[-2][0])/stack[-2][1]
            if len(stack) >= 2 and time2 >= time1:
                stack.pop()
        return len(stack)