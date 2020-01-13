"""Determine where in the conversation the uesr is, and return the necessary responses"""

def get_conversation_response(event_message):
    return get_feedback_posted_response(event_message)

def get_feedback_posted_response(event_message):
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
    
    # Return them to be sent 
    return post_to_channel, response_to_user
