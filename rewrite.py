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


about = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque possimus neque nobis animi quas ab delectus iure
eligendi saepe provident, eveniet culpa magni, consectetur labore expedita consequatur ipsum voluptatum voluptas!
Asperiores, ut ea accusamus debitis mollitia ex voluptatibus voluptates ipsam at nobis exercitationem assumenda
magni sed fugit ipsa aut minus quidem neque! Facere hic, est eveniet porro magni culpa, repellendus maxime tenetur
natus nisi animi ea distinctio consequatur quas fugiat ut deleniti aperiam? Saepe esse eligendi deserunt, aperiam
atque sunt ut dolore libero assumenda debitis commodi quisquam eius nisi sed? Dicta reiciendis nihil quidem quasi
vel saepe libero reprehenderit sunt."""

l_break = "\n-------------------------------------------------------------------------------------\n"


def about_the_software():
    print(f"{about}\n")
    input("Press Enter to continue...")
    print(l_break)
    select_source_label()
    return


def select_source_label():
    application_count = 1
    for label in custom_source_labels:
        print(f"{application_count}. {label['Application Name']}")
        application_count = application_count + 1
    user_input = input("\nSelect a custom label to use on your tweet: ")
    if user_input.isnumeric():
        if int(user_input) < application_count and int(user_input) > 0:
            print(l_break)
            write_tweet()
        else:
            selection_error()
    else:
        selection_error()


def write_tweet():
    print("write_tweet")
    return


def select_image():
    print("select_image")
    return


def review_tweet():
    print("review_tweet")
    return


def send_tweet():
    print("send_tweet")
    return


def selection_error():
    print(l_break)
    print(f"ERROR: INPUT SHOULD BE A LISTED NUMBER\n")
    select_source_label()


about_the_software()
