# -*- coding: utf-8 -*-
"""
Data 620
NLP and Crypto

Liam Byrne
Dimitriy Vecheruk

Twitter and BTC Data collection
"""

import got
import pandas as pd
import datetime  
from datetime import timedelta

# Time frames for tweet search
start_date = datetime.date(2017, 4, 1)
end_date = datetime.datetime.now().date()
days = (end_date - start_date).days

tweets = list()

# https://twitter.com/hashtag/Bitcoin?lang=en

# For each day, collect up to 1000 tweets that have #BTC OR #Bitcoin
for d in range(79, days):
    start = (start_date + timedelta(days = d)).strftime("%Y-%m-%d")
    end = (start_date + timedelta(days = d+1)).strftime("%Y-%m-%d")
    
    tweetCriteria = got.manager.TweetCriteria()\
        .setSince(start)\
        .setUntil(end)\
        .setQuerySearch("Bitcoin")\
        .setTopTweets(True)\
        .setMaxTweets(1000)
        
    tweets_handle = got.manager.TweetManager.getTweets(tweetCriteria)
    
    tweets.extend([(t.text, t.date) for t in tweets_handle])
    
    print(d)
    
tweets_df = pd.DataFrame(tweets, columns= ["tweet", "timestamp"])

# Remove unicode from Twitter
tweets_df.tweet = tweets_df.tweet.str.encode('utf-8')

tweets_df.to_csv("data/tweets2017.csv", index = False)
tweets_df.to_pickle("data/tweets2017.pkl")

# Get BTC->USD trades from the BitStamp exchange history file
inp = pd.read_csv("bitstampUSD.csv",names = ["timestamp","price", "volume"])

inp["date_time"]= pd.to_datetime(inp["timestamp"], unit='s')\
    .dt.tz_localize('UTC')\
    .dt.tz_convert('America/New_York')

btc = inp[inp["date_time"]>= "2017-04-01"]

btc.to_pickle("data/bitstampUSD_processed_2017.pkl",index=False)