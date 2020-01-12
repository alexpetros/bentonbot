import os
from slack import WebClient
from flask import request, Response

VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
BOT_USER_TOKEN = os.getenv("BOT_USER_TOKEN")
FEEDBACK_CHANNEL = "anon-feedback"

def post():

    # Get message
    slack_message = request.json
    print(slack_message)

    # Verify that the message comes from Slack
    if slack_message['token'] != VERIFICATION_TOKEN:
        return { 'status':403 }

    # If the request is the verification request, approve it 
    if slack_message['type'] == 'url_verification':
        return { 'data':slack_message, 'status':200 }

    # If the request is an event, process it
    if 'event' in slack_message:
        event_message = slack_message['event']

        # Ignore events that come from the bot itself 
        if 'subtype' in event_message and event_message['subtype'] == 'bot_message':
            return { 'status':200 }

        # Process message, and then let the method return OK 
        process_user_message(event_message)
    
    return { 'status':200 }

def process_user_message(event_message):
    user = event_message['user']
    text = event_message['text']
    channel = event_message['channel']

    # Create the bot's response for the user
    response_to_user = "Hi <@{}> :wave:\n".format(user)
    response_to_user += "I just send the following message to the directors:\n"
    response_to_user += "\"{}\"".format(text)

    # Create the bot's post in the feedback channel 
    post_to_channel = "Feedback sent in:\n"
    post_to_channel += text

    # Post message in anonymous feedback channel, and tell user it was sent
    Client = WebClient(BOT_USER_TOKEN)
    Client.chat_postMessage(channel=FEEDBACK_CHANNEL, text=post_to_channel)
    Client.chat_postMessage(channel=channel, text=response_to_user)
