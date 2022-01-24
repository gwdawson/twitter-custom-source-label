from dotenv import load_dotenv
import tweepy
import os
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('DEVICE_1_API_KEY'), os.getenv('DEVICE_1_API_KEY_SECRET'))
auth.set_access_token(os.getenv('DEVICE_1_ACCESS_TOKEN'), os.getenv('DEVICE_1_ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)
print (f'This tweet will be sent using the "TEMP NAME" source label\n')
tweet = input('What would you like to Tweet?: ')
api.update_status(status = (tweet))
print ('The tweet is live!')
