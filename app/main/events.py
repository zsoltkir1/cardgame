from flask import session
from flask_socketio import send, emit, join_room, leave_room
from .. import socketio
from app.main.model.card import Card
from random import randint

clients = 0
players = {}
hands = []
turns = {}
phases = {}
actualCard = {}

@socketio.on('joined', namespace='/chat')
def joined(message):
    global players
    global player
    global clients
    global turns
    global phases
    room = session.get('room')
    join_room(room)
    clients+=1
    hand=[Card(str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9))),Card(str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9))),Card(str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9))),Card(str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)))]
    hands.append(hand)
    session['player']=clients
    if session.get('room') in players:
        players[session.get('room')].append(clients)
    else:
        players[session.get('room')]=[]
        players[session.get('room')].append(clients)
    if len(players[session.get('room')])==1:
        turns[session.get('room')]='nothing'
        phases[session.get('room')]='nothing'
        actualCard[session.get('room')]='nothing'
    if len(players[session.get('room')])==2:
        turns[session.get('room')]='red'
        phases[session.get('room')]='select'
        actualCard[session.get('room')]='nothing'
    emit('status', {'msg': session.get('name') + ' csatlakozott a chatszobához.'}, room=room)
    print(room)
    print(session)
    print(phases[room])


@socketio.on('chatMessage', namespace='/chat')
def chatMessage():
    emit('my_response',{'name':session.get('player')},room=session.get('room'))


@socketio.on('text', namespace='/chat')
def text(message):  
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)
    #emit('message', {'msg': session.get('name') + message['msg']}, room=clients[0])


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': 'sorry srácok mennem kellett\n '+session.get('name') + ' kilépett.'}, room=room)


@socketio.on('chooseCard', namespace='/chat')
def chooseCard(i):
    global turns
    global actualCard
    global phases
    room = session.get('room')
    if phases[room]=='select':
        player = session.get('player')-1
        if player == 0 and turns[session.get('room')]=='red':
            tableID = 'tabl' + str(i['i']+1)
            actualCard = Card(hands[player][i['i']].top,hands[player][i['i']].bot,hands[player][i['i']].left,hands[player][i['i']].right,hands[player][i['i']].name)
            color="red"
            emit('choosenCard',{'tableID':tableID,'color':color,'card1top':actualCard.top,'card1bot':actualCard.bot,'card1left':actualCard.left,'card1right':actualCard.right,'card1name':actualCard.name},player=session.get('player'))
            turns[session.get('room')]="blue"
        elif player == 1 and turns[session.get('room')]=='blue':
            tableID = 'tabl' + str(i['i']+1)
            actualCard = Card(hands[player][i['i']].top,hands[player][i['i']].bot,hands[player][i['i']].left,hands[player][i['i']].right,hands[player][i['i']].name)
            color="blue"
            emit('choosenCard',{'tableID':tableID,'color':color,'card1top':actualCard.top,'card1bot':actualCard.bot,'card1left':actualCard.left,'card1right':actualCard.right,'card1name':actualCard.name},player=session.get('player'))
            turns[session.get('room')]="red"
        else:
            pass
    else:
        pass

#{'name':session.get('player')},room=session.get('room') #ezt még feltudom használni majd

@socketio.on('changeColor', namespace='/chat')
def changeColor(i):
    room = session.get('room')
    print(i)
    if i['i']==1:
        color="red"
    elif i['i']==2:
        color="blue"
    elif i['i']==0:
        color="green"
    else:
        color="pink"
    emit('changeColor2', {'color':color}, room=room)
    
@socketio.on('requestInitHand', namespace='/chat')
def initHand():
    player = session.get('player')-1
    emit('recieveInitHand', {'card1top':hands[player][0].top,'card1bot':hands[player][0].bot,'card1left':hands[player][0].left,'card1right':hands[player][0].right,'card1name':hands[player][0].name,'card2top':hands[player][1].top,'card2bot':hands[player][1].bot,'card2left':hands[player][1].left,'card2right':hands[player][1].right,'card2name':hands[player][1].name,'card3top':hands[player][2].top,'card3bot':hands[player][2].bot,'card3left':hands[player][2].left,'card3right':hands[player][2].right,'card3name':hands[player][2].name,'card4top':hands[player][3].top,'card4bot':hands[player][3].bot,'card4left':hands[player][3].left,'card4right':hands[player][3].right,'card4name':hands[player][3].name}, player=player)
    
    