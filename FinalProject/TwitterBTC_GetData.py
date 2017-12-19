"""
Data 620
NLP and Crypto

Liam Byrne
Dimitriy Vecheruk

Twitter and BTC Data collection
"""

import got3
"""
got3 available from
https://github.com/Jefferson-Henrique/GetOldTweets-python/tree/master/got3

For the got3 package, the url variable in the TweetManager.py file under /manager
was changed on line 91 from:
url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&%smax_position=%s"
to:
url = "https://twitter.com/i/search/timeline?f=news&q=%s&src=typd&%smax_position=%s"
in order to get the Tweeter News Feed
"""
import pandas as pd

import datetime
from datetime import timedelta


# Time frames for tweet search
start_date = datetime.date(2017, 4, 1)
end_date = datetime.datetime.now().date()
days = (end_date - start_date).days

tweets = list()


# For each day, collect up to 1000 tweets that have #BTC OR #Bitcoin
# Very long runtime (~6 hours)
for d in range(0, days):
    start = (start_date + timedelta(days = d)).strftime("%Y-%m-%d")
    end = (start_date + timedelta(days = d+1)).strftime("%Y-%m-%d")

    tweetCriteria = got3.manager.TweetCriteria()\
        .setSince(start)\
        .setUntil(end)\
        .setQuerySearch("Bitcoin OR BTC")\
        .setMaxTweets(1000)\
        .setLang("en")

    tweets_handle = got.manager.TweetManager.getTweets(tweetCriteria)

    tweets.extend([(t.text, t.date) for t in tweets_handle])

    print("{}: {} tweets collected".format(start, len(tweets_handle)

tweets_df = pd.DataFrame(tweets, columns= ["tweet", "timestamp"])

# Remove unicode from Twitter
tweets_df.tweet = tweets_df.tweet.str.encode('utf-8')

tweets_df.to_csv("data/tweetnews_2017.csv", index = False)
tweets_df.to_pickle("data/tweetnews_2017.pkl")

# Get BTC->USD trades from the BitStamp exchange history file
inp = pd.read_csv("bitstampUSD.csv",names = ["timestamp","price", "volume"])

inp["date_time"]= pd.to_datetime(inp["timestamp"], unit='s')\
    .dt.tz_localize('UTC')\
    .dt.tz_convert('America/New_York')

btc = inp[inp["date_time"]>= "2017-01-01"]

btc.to_pickle("data/bitstampUSD_processed_2017.pkl",index=False)
