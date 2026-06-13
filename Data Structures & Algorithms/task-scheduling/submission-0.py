import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        h = [-x for x in c.values()]
        time = 0
        queue=deque()
        heapq.heapify(h)
        while h or queue:
            time += 1
            if h:
                t = heapq.heappop(h)
                t += 1
                if t != 0:
                    queue.append([t,n+time])
            if queue and queue[0][1] == time:
                temp = queue.popleft()
                heapq.heappush(h, temp[0])
        return time
