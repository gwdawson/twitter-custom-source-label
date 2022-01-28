## README

_Before you are able to use this software you need a developer account on twitter. To acheive this just navigate to [Twitter Developer Platform](https://developer.twitter.com/) and fill out the application explaining what you want to do with their API. Once completed you will get an email letting you know if your application has been approved. After getting your approval from Twitter you can create your first app!_

## Creating A Twitter Application

- [x] Head over to [Twitter Developer Platform](https://developer.twitter.com/en/portal/projects-and-apps) and select "Create App".
- [x] Give your app a name, this is the name that will be shown on your tweets as the source label.
- [x] You will be redirected to API keys and Tokens, scroll down and click on “App Settings” to make few tweaks.
- [x] Scroll to App Permissions and change the option from “Read” to “Read and Write” and click on Save.
- [x] Scroll to Authentication Settings and turn on 3rd party authentication then click on Save.
- [x] Scroll to the top, and click on "Keys and Tokens" here you can see your Twitter API keys and Access Tokens.
- [x] Click on "Regenerate" for API Key & Secret then take a note of both Keys.
- [x] Click on "Generate" for Access Token & Secret then take a note of both Tokens.

## Setting Up The Software

- [x] At the top of this page select the green "Code" button and click "Download ZIP".
- [x] Extract the contents of the ZIP file to a folder called "twitter-custom-source-label".
- [x] Inside "twitter-custom-source-label", open "tweet.py" in your IDE or Text Editor.
- [x] On line 10 set the value of "device_1" to your application name and Save.
- [x] Open ".env" in your IDE or Text Editor, paste your Twitter API keys and Access Tokens and Save.

## Installing Python And Requirements

- [x] Go to [Python Downloads](https://www.python.org/downloads/) and select the latest version for your device.
- [x] Follow the setup guide until completely installed.
- [x] Once complete, navigate to "twitter-custom-source-label" in terminal/command prompt.
- [x] Run the following command `pip install -r requirements.txt`.
- [x] Finally you are on Mac or Linux run `python3 tweet.py`.
- [x] If you are on Windows run `Python tweet.py`.

## Sending Tweets With An Image

- [x] Replace "image.jpg" with the image you would like to send.
- [x] Make sure the new image is also called "image.jpg".
- [x] When asked in the software "Would you like to add an image to your tweet", select yes.

## License

This project is under the [MIT license](./LICENSE). See LICENSE for more details.

## Preview

![Screenshot](./config/screenshot.png?raw=true)
