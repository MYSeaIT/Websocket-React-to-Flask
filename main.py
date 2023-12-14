from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("Client connected")

@socketio.on('disconnect')
def test_disconnect():
    print("Client disconnected")

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    socketio.emit('response', {'data': 'Message received!'})

if __name__ == '__main__':
    socketio.run(app, debug=True)