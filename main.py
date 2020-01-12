from flask import Flask
from events import EventHandler 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def status_check():
    return "OK"

@app.route('/events', methods=['POST'])
def event_handler():
    print('handling event!')
    return EventHandler.post()

