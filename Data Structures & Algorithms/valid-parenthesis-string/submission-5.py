class Solution:
    def checkValidString(self, s: str) -> bool:
        paren_stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                paren_stack.append(i)
            if s[i] == "*":
                star_stack.append(i)
            if s[i] == ")":
                if paren_stack:
                    paren_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while paren_stack and star_stack:
            if paren_stack[-1] > star_stack[-1]:
                return False
            paren_stack.pop()
            star_stack.pop()
        return not paren_stack