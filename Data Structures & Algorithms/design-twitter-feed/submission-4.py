import heapq 
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        self.followMap[userId].add(userId)
        users = self.followMap[userId] | {userId}
        for i in users:
            if self.tweetMap[i]:
                idx = len(self.tweetMap[i])-1
                count, tweetId = self.tweetMap[i][idx]
                heapq.heappush(h,(count,tweetId,i,idx-1))
        res = []
        while h and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(h)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(h, (count,tweetId,followeeId,idx-1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
