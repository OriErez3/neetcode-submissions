class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(["+","-","*","/"])
        for i in tokens:
            if i not in operands:
                stack.append(i)
            elif i == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                temp = a + b
                stack.append(temp)
            elif i == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                temp = a - b
                stack.append(temp)
            elif i == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                temp = a * b
                stack.append(temp)
            elif i == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                temp = a / b
                stack.append(temp)
        return int(stack[0])
                    
                
                
        