class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [-1]*(len(s)+1)
        def dfs(i):
            if i > len(s)-1:
                return 1
            if cache[i] != -1:
                return cache[i]
            if s[i] == "0":
                return 0
            else:
                cache[i] = dfs(i+1)
                if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                    cache[i] += dfs(i+2)
                return cache[i]
        return dfs(0)