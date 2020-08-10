---
title: Data Crawling with Twitter API
description: Small project of data crawling.
categories:
  - web
cover: '/assets/images/intro_api/api.png'
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  API / Web / Data Crawling / Twitter
#header:
#  image: /assets/images/logos/logo-text-8c3ba8a6.svg
---
# Introduction
In the earlier post, I briefly introduced about how API and web work. In this post, let me talk about the practical usage of API: data crawling using Twitter API.

## Get Consumer Key (API key) and Access Key (Access token)

If you want access to Twitter’s APIs, you should create a twitter account (if you don't have one) and apply for a developer account using the new developer portal at [developer.twitter.com](https://developer.twitter.com/en).

If you want a help for steps in order to prevent to be banned, I recommend this [youtube instruction](https://www.youtube.com/watch?v=vlvtqp44xoQ)

Then, you should see Apps when you place your cursor on the account (right top corner in the figure shown below).
![tw_webpage](/assets/images/Data-Crawling-TwitterAPI/tw_webpage.png){:height="800px" width="600px"}  
| Fig1. Twitter Developer Portal|

From your Twitter Apps page, click `+ create App` and you are ready to go.
![tw_acc](/assets/images/Data-Crawling-TwitterAPI/tw_acc.png){:height="800px" width="400px"}  
| Fig2. Twitter Developer Portal|

## Open Source Libraries
The following libararies are open-source Python libraries for accessing Twitter API. I personally started with `tweepy`. 
- python-twitter by the Python-Twitter Developers
- tweepy by the tweepy Developers
- twitter by the Python Twitter Tools developer team
- TwitterSearch by @ckoepp
- twython by @ryanmcgrath and @mikehelmick
- TwitterAPI by @geduldig

## Streaming
First, I imported the necessary libraries and set the credentials (Consumer Key and Access Key).
> consumer_key (variable) is set as API key and access_key (variable) is set as Access token. Consumer API keys and Access token & access token secret) to authenticate with the API:

```python
import tweepy
from textblob import TextBlob
import preprocessor as prep
import statistics
from typing import List
```


```python
from secrets import consumer_key, consumer_secret, access_key, access_secret
# try doing this now:
auth= tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
```


```python
# for status in tweepy.Cursor(api.user_timeline, id='MACcosmetics', tweet_mode='extended').items():
#     print(status.full_text)
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth)

```


```python
# tweets = api.mentions_timeline()
# print(tweets)
```


```python
def get_tweets(keyword: str) -> List[str]:
    all_tweets=[]
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(10):
        all_tweets.append(tweet.full_text)
    return all_tweets

def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean=[]
    for tweet in all_tweets:
        tweets_clean.append(prep.clean(tweet))
    return tweets_clean

def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores=[]
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

def generate_average_sentiment_score(keyword: str) -> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    sentiment_scores = get_sentiment(tweets_clean)
    average_score = statistics.mean(sentiment_scores)
    return average_score

```


```python
if __name__ == '__main__':
    print('What does the world prefer?')
    first_thing = input()
    print('...or...')
    second_thing = input()
    print()
    first_score = generate_average_sentiment_score(first_thing)
    second_score = generate_average_sentiment_score(second_thing)
    if (first_score > second_score):
        print(f'the humanity prefers {first_thing} over {second_thing}!')
    else:
        print(f'the humanity prefers {second_thing} over {first_thing}')

```

    What does the world prefer?

     superman

    ...or...

     batman

    the humanity prefers batman over superman



```python
tweets = get_tweets('superman')
tweets
```




    ['RT @CristianT__T: The Best #superman 🧤🧤 https://t.co/UmXiDDQ4c4',
     '@DanSlott WATCHMEN\nPERSEPOLIS\nMAUS\nBATMAN YEAR ONE\nX-MEN GOD LOVES, MAN KILLS\nSECRET WARS\nIDENTITY CRISIS\nBATMAN BLACK MIRROR\nSPIDER-MAN SAGA OF THE ALIEN COSTUME\nALL-STAR SUPERMAN',
     '@FeathersandFoes I chose Superman on purpose. His stories are usually uplifting and pretty positive. If you get a chance, the first story arc post Infinite Crisis (one year later) is amazing.',
     '@DanSlott Dark Pheonix\nAll Star Superman\nSuperman: Secret Identity\nMister Miracle',
     '@cieItae the return of superman',
     "RT @Mister_Walsh: Watching Superman: The Movie as I draw today and it's got me itching for a new Supes movies that is full of hope and ligh…",
     'RT @DrPopCultureBG: Great Moments in Villainy\n\n#Superman https://t.co/c3kiDO213F',
     '@AdamTGorham @Mister_Walsh Frankly it’s the only parts of Snyder’s Superman I like. The flying scene in the arctic with soaring score. \n\nThen the rest happened.',
     'Great Moments in Villainy\n\n#Superman https://t.co/c3kiDO213F',
     'My superman T-shirt for for me on my birthday by my sweet little strawberry pie cup I love you dear https://t.co/GCrjm5nz69']




```python
tweets_clean=clean_tweets(tweets)
tweets_clean
```




    [': The Best',
     'WATCHMENPERSEPOLISMAUSBATMAN YEAR ONEX-MEN GOD LOVES, MAN KILLSSECRET WARSIDENTITY CRISISBATMAN BLACK MIRRORSPIDER-MAN SAGA OF THE ALIEN COSTUMEALL-STAR SUPERMAN',
     'I chose Superman on purpose. His stories are usually uplifting and pretty positive. If you get a chance, the first story arc post Infinite Crisis (one year later) is amazing.',
     'Dark PheonixAll Star SupermanSuperman: Secret IdentityMister Miracle',
     'the return of superman',
     ": Watching Superman: The Movie as I draw today and it's got me itching for a new Supes movies that is full of hope and ligh",
     ': Great Moments in Villainy',
     'Frankly its the only parts of Snyders Superman I like. The flying scene in the arctic with soaring score. Then the rest happened.',
     'Great Moments in Villainy',
     'My superman T-shirt for for me on my birthday by my sweet little strawberry pie cup I love you dear']



If you are interested in more detail information, please visit the following websites: [API](https://www.altexsoft.com/blog/engineering/what-is-api-definition-types-specifications-documentation/), [Web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
