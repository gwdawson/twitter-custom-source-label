from dotenv import load_dotenv
import tweepy
import os
import sys

load_dotenv()
os.system("clear")

number_of_devices = ["1", "2", "3"]
device_1 = "DUREX SmartCondom"
device_2 = "GUCCI SmartToilet"
device_3 = "Twitter for ArianaGrande"


def start_the_programme():
    user_selected_device = select_your_device()
    if not user_selected_device.isnumeric():
        error_select_number()
    else:
        if user_selected_device in number_of_devices:
            user_selected_image = select_image()
            if not user_selected_image.isnumeric():
                error_select_number()
            else:
                if user_selected_image == "1":
                    tweet_image_from_device(user_selected_device)
                elif user_selected_image == "2":
                    tweet_from_device(user_selected_device)
                else:
                    error_select_listed_number()
        else:
            error_select_listed_number()


def select_your_device():
    user_selected_device = str(
        input(
            f"""
What device would you like to tweet from?\n
0. Exit the programme
1. {device_1}
2. {device_2}
3. {device_3}\n
Select one number from above: """
        )
    )
    if user_selected_device == "0":
        sys.exit()
    else:
        return user_selected_device


def select_image():
    os.system("clear")
    user_selected_image = str(
        input(
            f"""
Would you like to add an image to your tweet?\n
1. Yes
2. No\n
Select one number from above: """
        )
    )
    return user_selected_image


def error_select_number():
    os.system("clear")
    print("------------------------------------------------------------")
    print("ERROR: Your input should be a number")
    print("------------------------------------------------------------")
    print("ERROR: The programme has been restarted")
    print("------------------------------------------------------------")
    start_the_programme()


def error_select_listed_number():
    os.system("clear")
    print("------------------------------------------------------------")
    print("ERROR: Your input should be a listed number")
    print("------------------------------------------------------------")
    print("ERROR: The programme has been restarted")
    print("------------------------------------------------------------")
    start_the_programme()


def tweet_from_device(user_selected_device):
    os.system("clear")
    auth = tweepy.OAuthHandler(
        os.getenv(f"DEVICE_{user_selected_device}_API_KEY"),
        os.getenv(f"DEVICE_{user_selected_device}_API_KEY_SECRET"),
    )
    auth.set_access_token(
        os.getenv(f"DEVICE_{user_selected_device}_ACCESS_TOKEN"),
        os.getenv(f"DEVICE_{user_selected_device}_ACCESS_TOKEN_SECRET"),
    )
    api = tweepy.API(auth)
    print(f'This tweet will be sent using the "TEMP NAME" source label\n')
    status = input("What would you like to Tweet?: ")
    api.update_status(status=status)
    print("The tweet is live!")


def tweet_image_from_device(user_selected_device):
    os.system("clear")
    auth = tweepy.OAuthHandler(
        os.getenv(f"DEVICE_{user_selected_device}_API_KEY"),
        os.getenv(f"DEVICE_{user_selected_device}_API_KEY_SECRET"),
    )
    auth.set_access_token(
        os.getenv(f"DEVICE_{user_selected_device}_ACCESS_TOKEN"),
        os.getenv(f"DEVICE_{user_selected_device}_ACCESS_TOKEN_SECRET"),
    )
    api = tweepy.API(auth)
    print(f'This tweet will be sent using the "TEMP NAME" source label\n')
    image = "image.jpg"
    status = input("What would you like to Tweet?: ")
    api.update_status_with_media(status, image)
    print("The tweet is live!")


start_the_programme()
