import socketio
import eventlet
from flask import Flask

sio = socketio.Server()

app = Flask(__name__)  # '__main__'


@sio.on('connect')  # message, disconnect
def connect(sid, environ):
    print('Connected')
    send_control(0, 1)

def send_control(steering_angle, throttle):
    #Event name in the udacity simulator
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })
if __name__ == "__main__":
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
