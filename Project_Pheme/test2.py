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

class mystuff:
	def average(self,a,b,c): #get the average of three numbers
		result=a+b+c
		result=result/3
		return result

x = mystuff()
x.average(9,18,27)
stream = '#fathersday'

class MyListener_s1(StreamListener):
    def on_status(self, status,stream):
        #listy.append(status)
        #print_ratios(listy)
        print(status.text)
        #z = clean_tweet(status.text)
        #print(twitter_stream.track)
        #x = get_tweet_sentiment(status.text)[0]
        #y = get_tweet_sentiment(status.text)[1]
        #if x != 'poes':
        # 	add_tweet(status.created_at,stream1,status.text.replace("'", ""),x,y)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        


def start_stream(stream):
	x = MyListener_s1()
	#x.on_status(status,stream)
	#with suppress(exceptions.ProtocolError):
	x.on_status(status,stream)
	twitter_stream = Stream(auth, x)
	twitter_stream.filter(track=[stream])

start_stream(stream)