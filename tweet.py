import tweepy
import config


user = 'TalebWisdom'
tweets = open('data/{}_to_tweet.txt'.format(user), encoding='utf8').readlines()

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

api.update_status(tweets.pop(0))

with open('data/{}_to_tweet.txt'.format(user), 'w', encoding='utf8') as writer:
    writer.writelines(tweets)
