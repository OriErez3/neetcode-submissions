class Solution:
    from collections import defaultdict, deque
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                
                d[pattern].append(word)  
        
        queue = deque()
        queue.append(beginWord)
        level_count = 0
        vist = set()
        while queue:
            level_count += 1
            for l in range(len(queue)):
                t = queue.popleft()
                if t == endWord:
                    return level_count
                vist.add(t)
                for i in range(len(t)):
                    pattern = t[:i]+"*"+t[i+1:]
                    for l in range(len(d[pattern])):
                        if d[pattern][l] not in vist:
                            vist.add(d[pattern][l])
                            queue.append(d[pattern][l])
        return 0   


           
            