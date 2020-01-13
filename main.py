from flask import Flask
from events import EventHandler 
from dotenv import load_dotenv

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

