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
#import matplotlib.pyplot as plt
from collections import defaultdict
import re
from contextlib import suppress
from urllib3 import exceptions
import threading


import os
import yaml

#direct = "/Users/user/"
direct = "/home/ubuntu/"
x_file = open(os.path.join(direct, "cred.yaml"), "r")
print(os.path.join(direct, "cred.yaml"))
docs = yaml.load(x_file)


charset = docs["db"]["charset"]
db = docs["db"]["db"]
host = docs["db"]["host"]
password = docs["db"]["password"]
user = docs["db"]["user"]

access_secret = docs["twitter"]["access_secret"]
access_token = docs["twitter"]["access_token"]
consumer_key = docs["twitter"]["consumer_key"]
consumer_secret = docs["twitter"]["consumer_secret"]
 
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
listy = []
temp_list = ["#bitcoin","#ethereum","#dash","crypto currency"]
stream1 = "#bitcoin"
stream2 = "#bitcoin"




def add_tweet(created_at,hashtag,text,sentiment_cat,sentiment_score):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host=host,
	user=user,
	password=password,
	db=db,
	charset=charset,
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
        
class MyListener_s2(StreamListener):
    def on_status(self, status):
        #listy.append(status)
        #print_ratios(listy)
        print(status.text)
        z = clean_tweet(status.text)
        #print(twitter_stream.track)
        x = get_tweet_sentiment(status.text)[0]
        y = get_tweet_sentiment(status.text)[1]
        if x != 'poes':
            add_tweet(status.created_at,stream2,status.text.replace("'", ""),x,y)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

class MyListener_s3(StreamListener):
    def on_status(self, status):
        #listy.append(status)
        #print_ratios(listy)
        print(status.text)
        z = clean_tweet(status.text)
        #print(twitter_stream.track)
        x = get_tweet_sentiment(status.text)[0]
        y = get_tweet_sentiment(status.text)[1]
        if x != 'poes':
            add_tweet(status.created_at,stream3,status.text.replace("'", ""),x,y)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

class MyListener_s4(StreamListener):
    def on_status(self, status):
        #listy.append(status)
        #print_ratios(listy)
        print(status.text)
        z = clean_tweet(status.text)
        #print(twitter_stream.track)
        x = get_tweet_sentiment(status.text)[0]
        y = get_tweet_sentiment(status.text)[1]
        if x != 'poes':
            add_tweet(status.created_at,stream4,status.text.replace("'", ""),x,y)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

class MyListener_s5(StreamListener):
    def on_status(self, status):
        #listy.append(status)
        #print_ratios(listy)
        print(status.text)
        z = clean_tweet(status.text)
        #print(twitter_stream.track)
        x = get_tweet_sentiment(status.text)[0]
        y = get_tweet_sentiment(status.text)[1]
        if x != 'poes':
            add_tweet(status.created_at,stream5,status.text.replace("'", ""),x,y)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

def start_stream(stream1,stream2):
	#while True:
		#try:
	with suppress(exceptions.ProtocolError):
			twitter_stream = Stream(auth, MyListener_s1())
			twitter_stream.filter(track=[stream1,stream2],async=True)
			#twitter2_stream = Stream(auth, MyListener_s2())
			#twitter2_stream.filter(track=[stream2], async=True)
		#except tweepy.TweepError:
		#	time.sleep(5)
		#	pass
def start_stream2(stream3,stream4):
    #while True:
        #try:
    with suppress(exceptions.ProtocolError):
            twitter_stream = Stream(auth, MyListener_s2())
            twitter_stream.filter(track=[stream3,stream4],async=True)


threads = []
t = threading.Thread(target=start_stream, args = (temp_list[0],temp_list[1],))
threads.append(t)
t.start()
t = threading.Thread(target=start_stream2, args = (temp_list[2],temp_list[3],))
threads.append(t)
t.start()


#twitter2_stream = Stream(auth, MyListener_s2())
#while True:
#	twitter2_stream.filter(track=[stream2], async=True)
#	
#twitter3_stream = Stream(auth, MyListener_s3())
#while True:
#	twitter3_stream.filter(track=[stream3], async=True)
