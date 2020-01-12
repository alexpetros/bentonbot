import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slack import WebClient

VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
BOT_USER_TOKEN = os.getenv("BOT_USER_TOKEN")
FEEDBACK_CHANNEL = "anon-feedback"

class Events(APIView):

    def __init__(self):
        self.client = WebClient(BOT_USER_TOKEN)

    def post(self, request, *args, **kwargs):

        # Get message
        slack_message = request.data

        # Verify that the message comes from Slack
        if slack_message.get('token') != VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # If the request is the verification request, approve it 
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message,
                            status=status.HTTP_200_OK)

        # If the request is an event, process it
        if 'event' in slack_message:
            event_message = slack_message.get('event')

            # Ignore events that come from the bot itself 
            if event_message.get('subtype') == 'bot_message':
                return Response(status=status.HTTP_200_OK)

            # Process message, and then let the method return OK 
            self.process_user_message(event_message)
        
        return Response(status=status.HTTP_200_OK)

    def process_user_message(self, event_message):
        user = event_message.get('user')
        text = event_message.get('text')
        channel = event_message.get('channel')

        # Create the bot's response for the user
        response_to_user = "Hi <@{}> :wave:\n".format(user)
        response_to_user += "I just send the following message to the directors:\n"
        response_to_user += "\"{}\"".format(text)

        # Create the bot's post in the feedback channel 
        post_to_channel = "Feedback sent in:\n"
        post_to_channel += text

        # Post message in anonymous feedback channel, and tell user it was sent
        self.client.chat_postMessage(channel=FEEDBACK_CHANNEL, text=post_to_channel)
        self.client.chat_postMessage(channel=channel, text=response_to_user)
