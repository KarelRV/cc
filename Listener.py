import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
 
consumer_key = 'nYxXmA9B7MmpgRdQBzg9LZxCp'
consumer_secret = 'cE5yAit3vEAIyQIyM69uGuSMAxjh9y8cPWXu7lyR8HF0EB02D4'
access_token = '45810954-CGIPoVv7cSkYLG5XsXFXLv2B4p5yfLfg3uF7EFUcc'
access_secret = '4SzUyUbAbTePDOjet7cw6AAOWwV41Wy9mZzdJV6TCpgYT'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
listy = []

 
class MyListener(StreamListener):
	def on_status(self, status):
		listy.append(status)
		print(status.created_at,status.text)

class MySaver(StreamListener): 
    def on_status(self, data):
        try:
            with open('bitcoin.json', 'a') as f:
                f.write(data.text)
                return True
        except BaseException as e:
            print(str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MySaver())
twitter_stream.filter(track=['#bitcoin'])
