from website import create_app, db
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from website.models import History
from flask_login import current_user
import random
from website.views import df

app = create_app()
socketio = SocketIO(app)

totalSongs = len(df.index) - 1

@socketio.on('connect')
def testConnect():
    print("connected")

@socketio.on('message')
def handleMessage(msg, room):
    message = History(message=msg, user_id=str(current_user))
    db.session.add(message)
    db.session.commit()
    print(msg)
    send(msg, room=room)

@socketio.on('join_room')
def joinRoom(roomName):
    join_room(roomName)
    print("joined room: " + roomName)
    send(current_user.first_name + " joined room " + roomName, room=roomName)

@socketio.on('leave_room')
def leaveRoom(roomName):
    leave_room(roomName)
    print("left room: " + roomName)
    send(current_user.first_name + " left room " + roomName, room=roomName)

@socketio.on("start_game")
def startGame(roomName):
    randVid = random.randint(0, totalSongs)
    print(randVid)
    socketio.emit("startGame", {"randVid": randVid}, room=roomName)

@socketio.on("get_rand")
def getRand(roomName):
    randVid = random.randint(0, totalSongs)
    print(randVid)
    socketio.emit("getRand", {"randVid": randVid}, room=roomName)

if __name__ == '__main__':
    socketio.run(app)