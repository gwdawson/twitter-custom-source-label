from dotenv import load_dotenv
import tweepy
import os
import sys

load_dotenv()

number_of_devices = ["1", "2", "3"]
device_1 = "DUREX SmartCondom"
device_2 = "GUCCI SmartToilet"
device_3 = "LG SmartRefrigerator"


def start_the_programme():
    user_input = select_your_device()
    if not user_input.isnumeric():
        error_select_number()
    else:
        if user_input in number_of_devices:
            tweet_from_device(user_input)
        else:
            error_select_listed_number()


def select_your_device():
    user_input = str(
        input(
            f"""
  What device would you like to tweet from?
  If you would like to quit type 'exit'.\n
  1. {device_1}
  2. {device_2}
  3. {device_3}\n
  Select one number from above: """
        )
    )
    if user_input.lower() == "exit":
        sys.exit()
    return user_input


def error_select_number():
    os.system("clear")
    print("---------------------------------")
    print("ERROR - Input should be a number!")
    print("---------------------------------\n")
    start_the_programme()


def error_select_listed_number():
    os.system("clear")
    print("----------------------------------------")
    print("ERROR - Input should be a listed number!")
    print("----------------------------------------\n")
    start_the_programme()


def tweet_from_device(user_input):
    os.system("clear")
    auth = tweepy.OAuthHandler(
        os.getenv(f"DEVICE_{user_input}_API_KEY"),
        os.getenv(f"DEVICE_{user_input}_API_KEY_SECRET"),
    )
    auth.set_access_token(
        os.getenv(f"DEVICE_{user_input}_ACCESS_TOKEN"),
        os.getenv(f"DEVICE_{user_input}_ACCESS_TOKEN_SECRET"),
    )
    api = tweepy.API(auth)
    print(f'This tweet will be sent using the "TEMP NAME" source label\n')
    tweet = input("What would you like to Tweet?: ")
    api.update_status(status=(tweet))
    print("The tweet is live!")


start_the_programme()
