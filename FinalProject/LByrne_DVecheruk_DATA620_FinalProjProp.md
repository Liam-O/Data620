[![CUNY_SPS](https://sps.cuny.edu/sites/all/themes/cuny/assets/img/header_logo.png)](https://sps.cuny.edu/academics/graduate/master-science-data-science-ms)

## Final Project Proposal for DATA 620 - Web Analytics (Fall 2017)

#### Liam Byrne
#### Dmitriy Vecheruk

***

## Cryptocurrency Price Evaluation and Natural Language Processing

### Motivation and Hypothesis

The value of cryptocurrencies, mainly Bitcoin ([BTC](https://coinmarketcap.com/currencies/bitcoin/)), have been extremely volatile since their inception. This volatility is spurred by speculation, future use cases and possibly by rumor and general sentiment. It would be an interesting use case of Natural Language Processing (NLP) to see how the cryptocurrency markets respond to news, rumor and overall sentiment; let's encapsulate all of these into sentiment for the sake of clarity. The result could be a gradation of the following:

1. Markets react to sentiment - *possible to capitalize on*
2. Sentiment is a reaction to the markets - *no use to capitalize on*
3. There is no correlation to either - *no use to capitalize on*

Moving forward, we will assume that **(1)** from above is how the markets react. The following will outline our problem statement, our tentative data sources and methods of creating a model.

### Business Understanding

For better or worse, social media has taken on the roles of a news source, an ever-present soap-box and a tool to influence markets. Utilizing social media data could allow for a better understanding of future market behavior. Picking a time to change one's position in the market has been described, analogously, to catching a falling knife for buying in or timing a swinging guillotine for selling. Being able to predict this timing better than the competition using the medium of social media could allow for larger monetary gains than the competition.

In order to explore news headlines and opinions about cryptocurrency and make a comparison to the trading price, we need to mine and aggregate social media data over a set time line (**Liam**) and then compare this information to the trading price (**Dmitriy**). We will analyze word usage and sentiment to construct a model in an attempt to forecast future pricing. Since Bitcoin is the most popular and the most valued cryptocurrency by market cap, it will be used as the proof of concept.

### Data Understanding
<p align="center">
<a href="https://twitter.com/">
  <img width="240" height="240" src="https://cdn2.iconfinder.com/data/icons/metro-uinvert-dock/256/Twitter_NEW.png">
</a>
</p>

The social media platform that will be mined is Twitter ([TWTR](https://finance.google.com/finance?q=NYSE:TWTR)) due to its large user base and its concise, 140 word limit. Historical Twitter data will be collected via the [Twitter API](https://developer.twitter.com/en/docs/tweets/search/api-reference/premium-search.html#DataEndpoint) or by the Python package [GetOldTweets](https://github.com/Jefferson-Henrique/GetOldTweets-python). Tweets mentioning Bitcoin (e.g. Bitcoin, #BTC, Satoshi) will be extracted from a given time period along with the tweet's time stamp. An initial exploration of word frequency will be explored. In addition, any oddities with the tweet data will try to be identified (e.g. if slang is predominately used,  do tweets appear to be from bots, etc.) (**Liam**).

<p align="center">
<a href="https://www.coindesk.com/">
  <img width="450" height="87" src="https://surveymonkey-assets.s3.amazonaws.com/survey/119070839/4b34c3c6-a1e4-4fa1-b045-fffed5a1c6f9.png">
</a>
</p>

Historical bitcoin decrease/increase percentages over the same timeline as above will be gathered from [CoinDesk](https://www.coindesk.com/price), which has historical pricing (date, time, open, high, low and close) over 15-minute intervals that can be exported to a csv, or [CoinDesk's API](https://www.coindesk.com/api/) from which historical prices can be requested. The data will be observed to note the format of time stamps and possible erroneous data (**Dmitriy**).

### Data Preparation

 The raw data from the tweets will need to be cleaned of erroneous Twitter data and stop words. The resulting cleaned data will be stored in a list tuple consisting of the tweet and the time stamp when the tweet was posted (**Liam**). Sentiment analysis (via [VADER](https://github.com/cjhutto/vaderSentiment)) for the tweet will be analyzed and the compound sentiment score will be appended to the respective tuple (**Dmitriy**).

 The trading price of BTC will categorized in one of the following manners:

 1. A method to produce a dependent categorical variable ``Up`` if the end-of-day closing price is above the opening price when the tweet was made. The method will assign ``Down`` if the opposite happens (**Dmitriy**).

 2. A method to build a quantile set of features (e.g.: ``+0% - +5%``, ``5% - 10%``, etc.) for the open/close differential after the tweet was made (**Dmitriy**).

 For either of the above, the features will be stored in a list of tuples with the resultant categorical variable and the opening time. (**Dmitriy**)

The above collection will be merged via a shared time stamp. This results in a list of tuples containing the tweets, the time stamp and the categorical dependent variable (**Dmitriy and Liam**). The time stamp is no longer needed for the future modeling phase, but it may be important to keep if any further analysis is needed.

### Modelling

Prior to choosing a model to use, data exploration will be used to look at word frequencies relative to the trading price (**Liam**) and the sentiment score relative to the trading price (**Dmitriy**) to see if any patterns are evident before we commit to the choice of model. Features may be added or subtracted as necessary depending on this data exploration phase (**Liam and Dmitriy**).

The resulting feature set, which includes:
1. High frequency words
2. Sentiment score
3. Categorized dependent variable
will be split (tentative 20% hold-out) and trained on up to two classifiers, naïve Bayes and random forest. (**Liam and Dmitriy**)

### Evaluation

The resultant accuracy and F-1 score of the model(s) will evaluated (**Liam and Dmitriy**). If the results are not marginally better than a coin flip, we will need to go back to the beginning of the modeling phase and try again.

It is said that if you torture data enough, it will speak, but we do not wish to get to level beyond water boarding, i.e., we are more concerned with seeing if there is a clear and relevant correlation between sentiment and trading price and if there isn't - explore reasons why our hypothesis is not correct.

### Deployment

Win or lose, we will summarize our findings in plots, tables or reports, so that our findings are consumable to a possible client (**Liam and Dmitriy**).

This final stage of the project will plan on showing that the team understood the scope of NLP covered over the course of the semester and was able to apply the learned techniques into a real-world use case. Even if our original hypothesis is wrong, i.e. sentiment is **not** a driving force behind cryptocurrency pricing, we believe that the exercise involved in reaching this conclusion will still show the understanding of the material covered and possible issues faced from the natural language processing process.

### References
<sup>[1]</sup> Cross-industry standard process for Data Mining (CRISP-DM). [https://www.wikiwand.com/en/Cross-industry_standard_process_for_data_mining](https://www.wikiwand.com/en/Cross-industry_standard_process_for_data_mining)
