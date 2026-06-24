from heapq import *

class Twitter:
    # self.timestamp = 0
    # map (postMap) of key: userId, value: queue of post tuples (timestamp, tweetId)
    # map (followingMap) of key: userId, value: who user is following (set)

    # post tweet -> create post tuple and add it to postMap
    # getNewsFeed -> create a list []
    # get posts from user, and posts from respective followingMap
    # combine into a list and then heapify
    # if length > 10: heappop()
    # reverse sort heap -> list = sorted(heap, reverse=True)
    # loop through list to get tweets to return

    # post, follow, unfollow is O(1) time
    # getNewsFeed is 

    def __init__(self):
        self.timestamp = 0
        self.postMap = defaultdict(list)
        self.followingMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        post = (self.timestamp, tweetId)
        self.postMap[userId].append(post)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        recentTweets = []
        tweets = []
        for post in self.postMap[userId]:
            tweets.append(post)

        for followee in self.followingMap[userId]:
            for post in self.postMap[followee]:
                tweets.append(post)

        heapify(tweets)
        while len(tweets) > 10:
            heappop(tweets)

        sortedTweets = sorted(tweets, reverse=True)
        for tweet in sortedTweets:
            recentTweets.append(tweet[1])
        return recentTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followingMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)
        
