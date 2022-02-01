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


def about_the_software():
    print(f"{about}\n")
    input("Press Enter to continue...")
    print("\n----------------------------------------------------------------------------------------------------\n")
    select_source_label()
    return


def select_source_label():
    print("select_source_label")
    return


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


about_the_software()
