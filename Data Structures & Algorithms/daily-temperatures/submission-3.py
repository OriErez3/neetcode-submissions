class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        new_temp = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx=stack.pop()
                new_temp[idx] = i-idx
            stack.append(i)
            
        return new_temp
            


            

            

        