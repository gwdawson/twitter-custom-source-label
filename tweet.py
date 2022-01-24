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

def start_the_programme():
  user_input = select_your_device()
  if not user_input.isnumeric():
    # Add error function here
    return
  else:
    if user_input == '1':
      tweet_from_device_1()
    elif user_input == '2':
      tweet_from_device_2()
    elif user_input == '3':
      tweet_from_device_3()
    elif user_input == '4':
      tweet_from_device_4()
    elif user_input == '5':
      tweet_from_device_5()
    elif user_input == '6':
      tweet_from_device_6()
    elif user_input == '7':
      tweet_from_device_7()
    elif user_input == '8':
      tweet_from_device_8()
    elif user_input == '9':
      tweet_from_device_9()
    else:
      # Add error function here
      return

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

def tweet_from_device_1():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_1_API_KEY'), os.getenv('DEVICE_1_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_1_ACCESS_TOKEN'), os.getenv('DEVICE_1_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_1}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

def tweet_from_device_2():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_2_API_KEY'), os.getenv('DEVICE_2_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_2_ACCESS_TOKEN'), os.getenv('DEVICE_2_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_2}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

def tweet_from_device_3():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_3_API_KEY'), os.getenv('DEVICE_3_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_3_ACCESS_TOKEN'), os.getenv('DEVICE_3_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_3}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

def tweet_from_device_4():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_4_API_KEY'), os.getenv('DEVICE_4_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_4_ACCESS_TOKEN'), os.getenv('DEVICE_4_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_4}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

def tweet_from_device_5():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_5_API_KEY'), os.getenv('DEVICE_5_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_5_ACCESS_TOKEN'), os.getenv('DEVICE_5_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_5}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

def tweet_from_device_6():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_6_API_KEY'), os.getenv('DEVICE_6_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_6_ACCESS_TOKEN'), os.getenv('DEVICE_6_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_6}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

def tweet_from_device_7():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_7_API_KEY'), os.getenv('DEVICE_7_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_7_ACCESS_TOKEN'), os.getenv('DEVICE_7_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_7}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

def tweet_from_device_8():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_8_API_KEY'), os.getenv('DEVICE_8_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_8_ACCESS_TOKEN'), os.getenv('DEVICE_8_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_8}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

def tweet_from_device_9():
  os.system('clear')
  auth = tweepy.OAuthHandler(os.getenv('DEVICE_9_API_KEY'), os.getenv('DEVICE_9_API_KEY_SECRET'))
  auth.set_access_token(os.getenv('DEVICE_9_ACCESS_TOKEN'), os.getenv('DEVICE_9_ACCESS_TOKEN_SECRET'))
  api = tweepy.API(auth)
  print (f'This tweet will be sent using the "{device_9}" source label\n')
  tweet = input('What would you like to Tweet?: ')
  api.update_status(status = (tweet))
  print ('The tweet is live!')

start_the_programme()
