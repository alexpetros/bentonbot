# Bentonbot
## Introduction
Basic slackbot to implement functionality in the DOC First Year Trips Slack. 

Named after the famous Doc Benton. Look out HES BEHIND YOU AHHH.

## Build instructions
### Starting the app
To run, first export the name of the flask app in the shell with `export FLASK_APP=main.py` then execute `pipenv run flask run`

Because the environment is managed my Pipenv, you can also run `pipenv shell` to enter the pipenv interactive environment, then you don't have to preempt commands with `pipenv run`. To exit the shell, simply type `exit`.

### Point to localhost
There are a number of ways to bind a localhost port to a public URL so that Slack can send events to it during testing. Personally, I use `ngrok`. With flask running on `localhost:5000`, use `ngrok http 5000` to get a URL that Slack can send event notifications to. Then add `<ngrok url>/events` to Slack's Event Subscriptions for that bot.

## Environmental configuration 
The bot won't be able to respond if you don't load the necessary authentication tokens into the environment. For development, simply create a `.env` file with the appropriate keys:
```
BOT_USER_TOKEN="xxx"
VERIFICATION_TOKEN="yyy"
FEEDBACK_CHANNEL="feedback-channel-name"
```

## TODO
* Some form of confirmation/conversation
* Anonymized user name for logs (mostly as an exercise)
* Move away from verification tokens to Slack secret keys
* Wrap the shell export and run into a single command
* Check that no duplicates were sent to the user or the channel
