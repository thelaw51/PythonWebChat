from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

print("Starting Flask app...")  # Add this line to check if script is being executed

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    print("Rendering index.html")
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('message', username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('message', username + ' has left the room.', room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)

