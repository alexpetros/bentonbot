"""Determine where in the conversation the uesr is, and return the necessary responses"""
from .constants import CONFIRMATION_RESPONSE

# TODO: parse history to enable confirmation
def get_conversation_response(event_message, history):
    return get_feedback_posted_response(event_message)

def get_feedback_posted_response(event_message):
    user = event_message['user']
    text = event_message['text']

    # Create the bot's response for the user
    response_to_user = "Hi <@{}>! I just sent the following message to the directors:\n".format(user)
    response_to_user += "\"{}\"".format(text)

    # Create the bot's post in the feedback channel 
    post_to_channel = "`<Feedback>`\n\n"
    post_to_channel += text
    
    # Return them to be sent 
    return post_to_channel, response_to_user

def get_confirmation_response(event_message):
    user = event_message['user']
    text = event_message['text']
    response_to_user = CONFIRMATION_RESPONSE
    response_to_user += ">{}".format(text)
    
