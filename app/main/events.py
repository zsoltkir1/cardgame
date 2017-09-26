from flask import session
from flask_socketio import send, emit, join_room, leave_room
from .. import socketio

clients = []

@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    clients.append('a')
    session['player']=len(clients)
    emit('status', {'msg': session.get('name') + ' csatlakozott a chatszobához.'}, room=room)


@socketio.on('sajatevent', namespace='/chat')
def sajatevent():
    emit('my_response',{'name':session.get('player')},room=session.get('room'))


@socketio.on('text', namespace='/chat')
def text(message):  
    #clients.append(request.sid)
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)
    #emit('message', {'msg': session.get('name') + message['msg']}, room=clients[0])
    


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': 'sorry srácok mennem kellett\n '+session.get('name') + ' kilépett.'}, room=room)

