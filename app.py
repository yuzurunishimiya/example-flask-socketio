from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import random
import time
import datetime

    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

data = [0,0,'00:00:00']

def get_random_data():
    data = [random.randint(0,100), random.randint(0,100)]
    return data

def get_time_now():
    now = datetime.datetime.now()
    in_this_day = f'{now.hour}:{now.minute}:{now.second}'
    return in_this_day

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('status')
def test_message(message):
    emit('data-receiver', data)


@socketio.on('data-access-new')
def access_new_data(latest_data):
    data = get_random_data()
    timenow = get_time_now()
    data.append(timenow)
    time.sleep(1)
    emit('data-receiver', data)


if __name__ == '__main__':
    socketio.run(app)
