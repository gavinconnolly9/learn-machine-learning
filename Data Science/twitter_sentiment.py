# Script to read the sentiment analysis of tweets containing a given word
# It measures the polarity(how positive or negative) and the subjectivity(how much of an opinion it is vs how factual) of the tweets
# https://github.com/llSourcell/twitter_sentiment_challenge
import tweepy
from textblob import TextBlob
import csv

# credentials for twitter
consumer_key = 	'6oBGmGT6MF9AeGtGqN3soeJHo'
consumer_secret = 'Uee1XMiSdBX9SlfRL71rM2ShKUQIt3I75Hds7NduXraOrADeIe'
access_token = '789887142-VSZFFA83GsTEdgSyp4Hxq55eMlTxYhRju7uGEyXq'
access_token_secret = '9TuFTbo4THFnVuwhHWCqW7dMwALYDPyKzORmTtPmxVMzT'

# to access twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# this method will retrieve a bunch of tweets containing 'Trump'
public_tweets = api.search('Trump')

with open('twitter_sentiment.csv', 'a') as csvfile:
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)

        if (analysis.sentiment.polarity >= 0):
            pol = 'positive'
        else:
            pol = 'negative'
        
        fields = [tweet.text, pol]
        writer = csv.writer(csvfile)
        writer.writerow(fields)




