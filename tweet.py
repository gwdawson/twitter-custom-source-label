from dotenv import load_dotenv
import tweepy
import os
load_dotenv()

device_1 = 'DUREX SmartCondom'
device_2 = 'GUCCI SmartToilet'
device_3 = 'LG SmartRefrigerator'
device_4 = ''
device_5 = ''
device_6 = ''
device_7 = ''
device_8 = ''
device_9 = ''

def select_your_device():
  user_input = str(input(f'''What device would you like to tweet from?\n
1. {device_1}
2. {device_2}
3. {device_3}
4. {device_4}
5. {device_5}
6. {device_6}
7. {device_7}
8. {device_8}
9. {device_9}
\nSelect one number from above: '''))
  return user_input

auth = tweepy.OAuthHandler(os.getenv('DEVICE_1_API_KEY'), os.getenv('DEVICE_1_API_KEY_SECRET'))
auth.set_access_token(os.getenv('DEVICE_1_ACCESS_TOKEN'), os.getenv('DEVICE_1_ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)
print (f'This tweet will be sent using the "TEMP NAME" source label\n')
tweet = input('What would you like to Tweet?: ')
api.update_status(status = (tweet))
print ('The tweet is live!')
