from website import create_app, db
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from website.models import History
from flask_login import current_user
import random, string

app = create_app()
socketio = SocketIO(app)

currentRoom = ""

def randomWord(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

@socketio.on('connect')
def testConnect():
    print("connected")

@socketio.on('message')
def handleMessage(msg):
    global currentRoom
    message = History(message=msg, user_id=str(current_user))
    db.session.add(message)
    db.session.commit()
    print(currentRoom)
    send(msg, broadcast=True)

@socketio.on('test')
def testMessage(msg):
    print("sdfsd " + msg)

# @socketio.on('create_room')
# def createRoom():
#     roomName = randomWord(5)
#     join_room(roomName)
#     currentRoom = roomName
#     print("created room: " + roomName)
#     send("Created room " + roomName, to=roomName)

@socketio.on('join_room')
def joinRoom(roomName):
    global currentRoom
    join_room(roomName)
    print("joined room: " + roomName)
    currentRoom = roomName
    send(current_user.first_name + " joined room " + roomName, broadcast=True)

if __name__ == '__main__':
    #app.run(debug=True)
    socketio.run(app)