import sys


class Response:
    def __init__(self, tweet, polarity, subjectivity):
        self.tweet = tweet
        self.polarity = polarity
        self.subjectivity = subjectivity

    def getTweet(self):
        return self.tweet

    def getPolarity(self):
        return self.polarity

    def getSubjectivity(self):
        return self.subjectivity
