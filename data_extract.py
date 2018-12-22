import tweepy
import logging
import json
import config

from tweepy import Stream
from tweepy.streaming import StreamListener

# logging.basicConfig(level=logging.DEBUG)

# Setup Twitter API
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Stream Listener
class MyListener(StreamListener):
    def on_data(self,data):
        try:
            with open('data.json','a') as  f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" %str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

# Function used to make the stream for storing the data into
# the file which contains the particular keyword
def retrieve_keyword_tweet(keyword):
        twitter_stream = Stream(auth,MyListener())
        twitter_stream.filter(track=[keyword])
