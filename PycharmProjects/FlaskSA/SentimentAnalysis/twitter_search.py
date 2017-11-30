import tweepy
from textblob import TextBlob
from SentimentAnalysis.Response import Response
class TwitterSearch(object):
    def __init__(self):
        self.consumer_key = "eApt3gfqplZ4OJBAgEAfjL4gL"
        self.consumer_secret = "Sjcxh82mjGPZNNclfgrDRl7DNtnnhbuTGwIRA81d4jjQL4KHGH"
        self.access_token = "924779675552849920-oVxdr5kmvnveUPG8MOaQCIOBDKtbKMG"
        self.access_level = "tBb9t7mG41TYOk3ebgULZRVoyisvXMK4wa3l1q0gl4pPG"

    def search(self, query):


        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_level)

        api = tweepy.API(auth)

        public_tweets = api.search(query)
        tweet_list = []
        for tweet in public_tweets:
            print(tweet.text)
            analysis = TextBlob(tweet.text)
            response = Response(tweet.text, analysis.subjectivity, analysis.polarity)
            tweet_list.append(response)
        return tweet_list