import tweepy
import os

os.system("clear")


custom_source_labels = [
    {
        "Application Name": "",
        "API KEY": "",
        "API KEY SECRET": "",
        "ACCESS TOKEN": "",
        "ACCESS TOKEN SECRET": "",
    },
    {
        "Application Name": "",
        "API KEY": "",
        "API KEY SECRET": "",
        "ACCESS TOKEN": "",
        "ACCESS TOKEN SECRET": "",
    },
    {
        "Application Name": "",
        "API KEY": "",
        "API KEY SECRET": "",
        "ACCESS TOKEN": "",
        "ACCESS TOKEN SECRET": "",
    },
]

l_break = "\n-------------------------------------------------------------------------------------\n"
user_selected_application = ""
user_typed_tweet = ""
user_selected_image = ""


def about_the_software():
    print(
        """Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque possimus neque nobis animi quas ab delectus iure
eligendi saepe provident, eveniet culpa magni, consectetur labore expedita consequatur ipsum voluptatum voluptas!
Asperiores, ut ea accusamus debitis mollitia ex voluptatibus voluptates ipsam at nobis exercitationem assumenda
magni sed fugit ipsa aut minus quidem neque! Facere hic, est eveniet porro magni culpa, repellendus maxime tenetur
natus nisi animi ea distinctio consequatur quas fugiat ut deleniti aperiam? Saepe esse eligendi deserunt, aperiam
atque sunt ut dolore libero assumenda debitis commodi quisquam eius nisi sed? Dicta reiciendis nihil quidem quasi
vel saepe libero reprehenderit sunt.\n"""
    )
    input("Press Enter to continue...")
    print(l_break)
    select_source_label()


def select_source_label():
    application_count = 1
    for label in custom_source_labels:
        print(f"{application_count}. {label['Application Name']}")
        application_count = application_count + 1
    user_input = input("\nSelect a custom label to use on your tweet: ")
    if len(str(user_input)) > 0:
        if str(user_input).isnumeric():
            if int(user_input) < application_count and int(user_input) > 0:
                global user_selected_application
                user_selected_application = custom_source_labels[int(user_input) - 1][
                    "Application Name"
                ]
                print(l_break)
                write_tweet()
            else:
                error(1, "select_source_label")
        else:
            error(1, "select_source_label")
    else:
        error(1, "select_source_label")


def write_tweet():
    global user_selected_application
    global user_typed_tweet
    user_typed_tweet = input("Enter your tweet: ")
    if len(user_typed_tweet) > 0:
        if len(user_typed_tweet) < 280:
            print(l_break)
            select_image()
        else:
            error(3, "write_tweet")
    else:
        error(2, "write_tweet")


def select_image():
    global user_selected_image
    user_selected_image = input("1. Yes\n2. No\n\nWould you like to add an image: ")
    if len(str(user_selected_image)) > 0:
        if str(user_selected_image).isnumeric():
            if int(user_selected_image) == 1:
                print(l_break)
                print(
                    "MAKE SURE YOUR IMAGE IS LOCATED IN /twitter-custom-source-label/images/\n"
                )
                user_selected_image_name = input(
                    "What is the name of your image file: "
                )
                if len(user_selected_image_name) > 0:
                    if user_selected_image_name.endswith(
                        ".png"
                    ) or user_selected_image_name.endswith(".jpg"):
                        user_selected_image = user_selected_image_name
                        print(l_break)
                        review_tweet()
                    else:
                        error(4, "select_image")
                else:
                    error(2, "select_image")
            elif int(user_selected_image) == 2:
                user_selected_image = False
                print(l_break)
                review_tweet()
            else:
                error(1, "select_image")
        else:
            error(1, "select_image")
    else:
        error(1, "select_image")


def review_tweet():
    print(
        f"Application Name: {user_selected_application}\nTweet: {user_typed_tweet}\nimage: {user_selected_image}\n"
    )
    user_send_tweet = input(f"1. Yes\n2. No\n\nWould you like to send this tweet: ")
    if len(user_send_tweet) > 0:
        if user_send_tweet.isnumeric():
            if int(user_send_tweet) == 1:
                print(l_break)
                send_tweet()
            elif int(user_send_tweet) == 2:
                exit()
            else:
                error(1, "review_tweet")
        else:
            error(1, "review_tweet")
    else:
        error(2, "review_tweet")


def send_tweet():
    global user_selected_image
    global user_typed_tweet
    for i in custom_source_labels:
        if i["Application Name"] == user_selected_application:
            application_object = i
    if user_selected_image == False:
        auth = tweepy.OAuthHandler(
            application_object["API KEY"], application_object["API KEY SECRET"]
        )
        auth.set_access_token(
            application_object["ACCESS TOKEN"],
            application_object["ACCESS TOKEN SECRET"],
        )
        api = tweepy.API(auth)
        api.update_status(status=user_typed_tweet)
        print("The tweet is live!")
        return
    else:
        auth = tweepy.OAuthHandler(
            application_object["API KEY"], application_object["API KEY SECRET"]
        )
        auth.set_access_token(
            application_object["ACCESS TOKEN"],
            application_object["ACCESS TOKEN SECRET"],
        )
        api = tweepy.API(auth)
        user_selected_image = "./images/" + user_selected_image
        api.update_status_with_media(user_typed_tweet, user_selected_image)
        print("The tweet is live!")
        return


def error(num, function=None):
    if num == 1:
        print(l_break)
        print(f"ERROR: INPUT SHOULD BE A LISTED NUMBER\n")
        error_return(function)
    elif num == 2:
        print(l_break)
        print(f"ERROR: INPUT SHOULD BE MORE THAN 0 CHARACTERS\n")
        error_return(function)
    elif num == 3:
        print(l_break)
        print(f"ERROR: INPUT SHOULD BE LESS THAN 280 CHARACTERS\n")
        error_return(function)
    elif num == 4:
        print(l_break)
        print(f"ERROR: INPUT SHOULD END WITH .PNG OR .JPG\n")
        error_return(function)
    else:
        os.system("clear")
        exit()
        print("An Unexpected Error Occurred")


def error_return(function):
    if function == "select_source_label":
        select_source_label()
    elif function == "write_tweet":
        write_tweet()
    elif function == "select_image":
        select_image()
    elif function == "review_tweet":
        review_tweet()
    elif function == "send_tweet":
        send_tweet()


about_the_software()
