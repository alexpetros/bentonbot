from flask import Flask
from dotenv import load_dotenv

from bentonbot import EventHandler 

app = Flask(__name__)

# Load environmental constants
load_dotenv()

@app.route('/', methods=['GET'])
def status_check():
    return "OK"

@app.route('/events', methods=['POST'])
def event_handler():
    print('handling event!')
    return EventHandler.post()

