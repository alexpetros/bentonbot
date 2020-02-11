import os
from slack import WebClient
from flask import request, Response

from .ConversationHandler import get_conversation_response

# Runtime constants
VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
BOT_USER_TOKEN = os.getenv("BOT_USER_TOKEN")
FEEDBACK_CHANNEL = os.getenv("FEEDBACK_CHANNEL")

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
        user_dm_channel = event_message['channel']

        # Ignore events that come from the bot itself 
        if 'subtype' in event_message and event_message['subtype'] == 'bot_message':
            return { 'status':200 }

        # Process message, and then let the method return OK 
        Client = WebClient(BOT_USER_TOKEN)
        history = Client.conversations_history(channel=user_dm_channel)
        post_to_channel, response_to_user = get_conversation_response(event_message, history)

        # Post message in anonymous feedback channel, and tell user it was sent
        Client.chat_postMessage(channel=FEEDBACK_CHANNEL, text=post_to_channel)
        Client.chat_postMessage(channel=user_dm_channel, text=response_to_user)
    
    return { 'status':200 }

