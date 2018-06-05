import tweepy
from secrets import *
from random import randint

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

tweet = "Base Message for a Tweet :)"

api.update_status(tweet)