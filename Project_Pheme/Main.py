import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
import json
import operator 
from collections import Counter
from nltk.corpus import stopwords
import string
import nltk
import pandas as pd
from nltk import bigrams 
import matplotlib.pyplot as plt
from collections import defaultdict
import re
from contextlib import suppress
from urllib3 import exceptions
import threading

 
consumer_key = 'nYxXmA9B7MmpgRdQBzg9LZxCp'
consumer_secret = 'cE5yAit3vEAIyQIyM69uGuSMAxjh9y8cPWXu7lyR8HF0EB02D4'
access_token = '45810954-CGIPoVv7cSkYLG5XsXFXLv2B4p5yfLfg3uF7EFUcc'
access_secret = '4SzUyUbAbTePDOjet7cw6AAOWwV41Wy9mZzdJV6TCpgYT'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
listy = []
temp_list = ["#bitcoin","#ethereum","#DASH"]
stream1 = "#bitcoin"
stream2 = "#LeMans24"
stream3 = "#ConFedCup"




def add_tweet(created_at,hashtag,text,sentiment_cat,sentiment_score):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='pheme.cenvzddeh7ne.eu-west-1.rds.amazonaws.com',
	user='PhemeUES528',
	password='^d+L6s_yc<_TC%6',
	db='Pheme',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "insert into  tweets values(NULL,'{0}','{1}', '{2}', '{3}', '{4}')".format(created_at,hashtag,text,sentiment_cat,sentiment_score)
		cursor.execute(sql)
		connection.commit()
	connection.close()



def get_tweet_sentiment(tweet):
	
	if len(clean_tweet(tweet)) >= 10:
		analysis = TextBlob(clean_tweet(tweet))
		#print(analysis.detect_language())
		#if analysis.detect_language() == 'en':
		# set sentiment
		if analysis.sentiment.polarity > 0:
			return 'positive',analysis.sentiment.polarity
		elif analysis.sentiment.polarity == 0:
			return 'neutral',analysis.sentiment.polarity
		else:
			return 'negative',analysis.sentiment.polarity
		#else:
			#return 'poes',0.0
	else:
		return 'poes',0.0


def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet(listy):
    tweets = []
    for tweet in listy:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
    
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text)
    
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
    return(tweets)

def print_ratios(listy):
    tweets = get_tweet(listy)
    print(len(tweets))
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print("Positive: {} %".format(100*len(ptweets)/len(tweets)),
      "Negative: {} %".format(100*len(ntweets)/len(tweets)),
      "Neutral:{}%".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))
     )    
 
class MyListener_s1(StreamListener):
    def on_status(self, status):
        #listy.append(status)
        #print_ratios(listy)
        print(status.text)
        z = clean_tweet(status.text)
        #print(twitter_stream.track)
        x = get_tweet_sentiment(status.text)[0]
        y = get_tweet_sentiment(status.text)[1]
        if x != 'poes':
        	add_tweet(status.created_at,stream1,status.text.replace("'", ""),x,y)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        


def start_stream(stream):
	#while True:
		#try:
	with suppress(exceptions.ProtocolError):
			twitter_stream = Stream(auth, MyListener_s1())
			twitter_stream.filter(track=[stream],async=True)
			#twitter2_stream = Stream(auth, MyListener_s2())
			#twitter2_stream.filter(track=[stream2], async=True)
		#except tweepy.TweepError:
		#	time.sleep(5)
		#	pass

threads = []

for i in temp_list:
    t = threading.Thread(target=start_stream, args = (i,))
    threads.append(t)
    t.start()

#twitter2_stream = Stream(auth, MyListener_s2())
#while True:
#	twitter2_stream.filter(track=[stream2], async=True)
#	
#twitter3_stream = Stream(auth, MyListener_s3())
#while True:
#	twitter3_stream.filter(track=[stream3], async=True)
