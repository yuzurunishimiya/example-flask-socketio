from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

import datetime
import random
import time

    
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

@app.route('/api/store-single-data', methods=['POST'])
def single_data():
    global data
    json_data = request.get_json()
    data = json_data['data']
    return json_data['status']


@socketio.on('status')
def test_message(message):
    emit('data-receiver', data)


@socketio.on('data-access-new')
def access_new_data(latest_data):
    time.sleep(1)
    emit('data-receiver', data)


if __name__ == '__main__':
    socketio.run(app)
