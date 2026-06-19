class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_score = [0]*(n+1)
        for a,b in trust:
            trust_score[a] -= 1
            trust_score[b] += 1
        return trust_score.index(n-1) if n-1 in trust_score else -1
