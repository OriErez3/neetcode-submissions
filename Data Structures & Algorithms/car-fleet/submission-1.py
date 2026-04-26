class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = zip(position, speed)
        posSpeed = sorted(posSpeed, reverse=True)
        stack = []
        for i in posSpeed:
            time = (target - i[0])/i[1]
            if not stack:
                stack.append(time)
            if stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)