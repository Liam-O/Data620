[![N|Solid](https://sps.cuny.edu/sites/all/themes/cuny/assets/img/header_logo.png)](https://sps.cuny.edu/academics/graduate/master-science-data-science-ms)

## Final Project Proposal for DATA 620 - Web Analytics (Fall 2017)
##### Liam Byrne
##### Dmitriy Vecheruk
***
## Cryptocurrency Price Evaluation and Natural Language Processing
### Motivation and Hypothesis
The value of cryptocurrencies, mainly Bitcoin ([BTC](https://coinmarketcap.com/currencies/bitcoin/)), have been extremely volatile since their inception. This volatility is spurred by speculation, future use cases and most importantly by rumor and sentiment. It would be an interesting use case of Natural Language Processing (NLP) to see how the cryptocurrency markets respond to news, rumor and overall sentiment; let's encapsulate everything into sentiment for the sake of clarity. The result could be a gradation of the following:

1. Markets react to sentiment - *possible to capitalize on*
2. Sentiment is a reaction to the markets - *no use to capitalize on*
3. There is no correlation to either - *no use to capitalize on*

Moving forward, we will assume that **(1)** from above is how the markets react. We will analyze word usage and sentiment and construct a model that can forecast future pricing. Since Bitcoin is the most popular and most valued cryptocurrency by market cap, it will be used as the proof of concept. The following will outline our tentative data sources, methods and problems foreseen in creating a model.

### Methods and Data Sources
[![Twitter](https://cdn2.iconfinder.com/data/icons/metro-uinvert-dock/256/Twitter_NEW.png)](https://twitter.com/)[![Coindesk](https://daks2k3a4ib2z.cloudfront.net/576d13c8eb5794cb5888fc50/59d232e085c6930001f4cb11_CoinDesk_WEB.png)](https://www.coindesk.com/price/)

The general approach will be as follows:

1. Extract historical Twitter ([TWTR](https://finance.google.com/finance?q=NYSE:TWTR)) data via the [Twitter API](https://developer.twitter.com/en/docs/tweets/search/api-reference/premium-search.html#DataEndpoint). Tweets mentioning Bitcoin (e.g. Bitcoin, BTC, #BTC) will be extracted from a given time period, time stamped and processed.
2. Collect historical bitcoin decrease/increase percentages over same timeline. [Coindesk](https://www.coindesk.com/price) has historical pricing (date, time, open, high, low and close) over 15-minute intervals that will be exported to a csv.
3. Offset the price differential by a fixed point in the future relative to when the tweet was made (e.g. the open/close differential for the day starting a half hour after the tweet was made).
   a. If a classifier is being used, the price differentials will be stratified into groups (e.g. up/down or some percentage quantile).
4. A combination of some or all of the following will be used:
) Analyze tweet sentiments (most likely via [VADER](https://github.com/cjhutto/vaderSentiment)) in relation to the future price differential in order to explore sentiment and market prices.
   b. Construct a document term matrix then feature extract common words. Using a classifier, e.g. Naive Bayes, analyze most important features in relation to price prediction.
   c. Split data into testing and training sets and use some method f machine learning to see how any of the above (**a** or **b**) perform.

### Foreseen Problems
**Data Collection**
The free (premium) version of the Twitter Search API only allows for searching up to thirty (30) days back in time for historical (non-streaming) tweets. In addition, the API has a rate limit that can easily be exceeded if careful attention is not paid to it. Python has tools to slow requests to not exceed a set limit. If the API is really troublesome or the data within the 30-day envelope is not conclusive (possible with the ~100% jump in price in the last 30 days as of the writing of this), there are Python packages that bypass the API (e.g. the [GetOldTweets](https://github.com/Jefferson-Henrique/GetOldTweets-python) that will be explored if the "orthodox" avenue of data collection is not working.

**Useful Data (avoiding GIGO)**
Exploring key historical points (e.g. periods of exchange hacks or government intervention) in Bitcoin's timeline may be necessary to train a better model, analyze key phrases in tweets or get more varied sentiment

### Planned Outcome
At the very least, we will incorporate a lot of what we learned over the course of the semester to create something with a real-world use case. Even if our original hypothesis is wrong, i.e. sentiment is **not** a driving force behind cryptocurrency pricing), we believe that the exercise involved in reaching this conclusion will still utilize most skills garnered in the class and could be adaptable to other real-world applications of natural language processing.