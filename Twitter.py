from collections import deque, defaultdict
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetids=defaultdict(list)
        self.tweetfeed=list()
        self.followerid=defaultdict(list)
        self.followeeid=defaultdict(list)
        self.recent=defaultdict(deque)

    def addRecent(self, userId, tweetId):
        """
        Add a new tweet to recent buffer.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if len(self.recent[userId]) >= 10:
            self.recent[userId].pop()    
        self.recent[userId].appendleft(tweetId)

        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweetids[userId].append(tweetId)
        self.tweetfeed.append([tweetId,userId])
        self.addRecent(userId,tweetId)
        for fid in self.followerid[userId]:
            self.addRecent(fid,tweetId)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        return list(self.recent[userId])
    
    def merge(self, followerId):
        self.recent[followerId].clear()
        for i in range(len(self.tweetfeed)-1,-1,-1):
            t = self.tweetfeed[i]
            if t[1] == followerId or t[1] in self.followeeid[followerId]:
                self.recent[followerId].append(t[0]) 
            if len(self.recent[followerId]) == 10:
                break
    
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followerid[followeeId] or followerId == followeeId:
            return
        self.followerid[followeeId].append(followerId)
        self.followeeid[followerId].append(followeeId)
        self.merge(followerId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if self.followerid[followeeId].count(followerId) > 0:
            self.followerid[followeeId].remove(followerId)
            self.followeeid[followerId].remove(followeeId)
            for tid in self.tweetids[followeeId]:
                if self.recent[followerId].count(tid) >0:
                    self.recent[followerId].remove(tid)
            if len(self.recent[followerId]) < 10:
                self.merge(followerId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeefolloweeIdId)
# obj.unfollow(followerId,followeeId)