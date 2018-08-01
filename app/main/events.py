from flask import session
from flask_socketio import send, emit, join_room, leave_room
from .. import socketio
from app.main.model.card import Card
from app.main.dao import CardService
from random import randint,randrange

clients = 0
clientsInRoom = {}
players = {}
hands = []
boards = {}
turns = {}
db = {}
phases = {}
actualCard = {}
decks = {}

@socketio.on('joined', namespace='/chat')
def joined(message):
    global players
    global player
    global clients
    global clientsInRoom
    global turns
    global phases
    global db
    global decks
    room = session.get('room')
    join_room(room)
    clients+=1
    if session.get('room') in clientsInRoom:
        clientsInRoom[session.get('room')].append(clients)
    else:
        clientsInRoom[session.get('room')]=[]
        clientsInRoom[session.get('room')].append(clients)
    #hand=[Card(str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9))),Card(str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9))),Card(str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9))),Card(str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)),str(randint(1, 9)))]
    session['player']=clients
    decks[session.get('player')]=CardService().initDeck()
    hand=[decks[session.get('player')].pop(randrange(len(decks[session.get('player')]))),decks[session.get('player')].pop(randrange(len(decks[session.get('player')]))),decks[session.get('player')].pop(randrange(len(decks[session.get('player')]))),decks[session.get('player')].pop(randrange(len(decks[session.get('player')])))]
    print(decks[session.get('player')]) 
    hands.append(hand)   
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
        db[room]=1
        turns[session.get('room')]='red'
        phases[session.get('room')]='select'
        actualCard[session.get('room')]='nothing'
    emit('status', {'msg': session.get('name') + ' csatlakozott a chatszobához.'}, room=room)
    print(room)
    print(session)
    print(phases[room])
    for k in range(5):
        for l in range(5):
            try:
                emit('boardDraw',{'top':boards[room,k,l][0].top,'bot':boards[room,k,l][0].bot,'left':boards[room,k,l][0].left,'right':boards[room,k,l][0].right,'name':boards[room,k,l][0].name,'topname':'intd'+str(k+1)+str(l+1)+'12','botname':'intd'+str(k+1)+str(l+1)+'32','leftname':'intd'+str(k+1)+str(l+1)+'21','rightname':'intd'+str(k+1)+str(l+1)+'23','namename':'intd'+str(k+1)+str(l+1)+'22','color':boards[room,k,l][1],'tableID':'tabl'+str(k+1)+str(l+1)},room=room)
            except:
                pass


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
    global phases
    global actualCard
    global clientsInRoom
    room = session.get('room')
    if phases[room]=='select':
        player = session.get('player')-1
        if player == clientsInRoom[room][0]-1 and turns[session.get('room')]=='red':
            tableID = 'tabl' + str(i['i']+1)
            actualCard[room] = Card(hands[player][i['i']].name,hands[player][i['i']].top,hands[player][i['i']].bot,hands[player][i['i']].left,hands[player][i['i']].right),i['i']
            color="red"
            emit('choosenCard',{'tableID':tableID,'color':color,'card1top':actualCard[room][0].top,'card1bot':actualCard[room][0].bot,'card1left':actualCard[room][0].left,'card1right':actualCard[room][0].right,'card1name':actualCard[room][0].name},player=session.get('player'))
            #turns[session.get('room')]="green"
            phases[room]='put'
        elif player == clientsInRoom[room][1]-1 and turns[session.get('room')]=='green':
            tableID = 'tabl' + str(i['i']+1)
            actualCard[room] = Card(hands[player][i['i']].name,hands[player][i['i']].top,hands[player][i['i']].bot,hands[player][i['i']].left,hands[player][i['i']].right),i['i']
            color="green"
            emit('choosenCard',{'tableID':tableID,'color':color,'card1top':actualCard[room][0].top,'card1bot':actualCard[room][0].bot,'card1left':actualCard[room][0].left,'card1right':actualCard[room][0].right,'card1name':actualCard[room][0].name},player=session.get('player'))
            #turns[session.get('room')]="red"
            phases[room]='put'
        else:
            pass
    else:
        pass

#{'name':session.get('player')},room=session.get('room') #ezt még feltudom használni majd

@socketio.on('putCard', namespace='/chat')
def putCard(i,j):
    global turns
    global phases
    global actualCard
    global boards
    global db
    room = session.get('room')
    player = session.get('player')-1
    if phases[room]=='put':
        if player == clientsInRoom[room][0]-1 and turns[session.get('room')]=='red' and (room,i['i'],j['j']) not in boards:
            boards[room,i['i'],j['j']]=[actualCard[room][0],turns[room]]
            tableID = 'tabl' + str(i['i']+1) + str(j['j']+1)
            top='intd'+ str(i['i']+1) + str(j['j']+1) + '12'
            bot='intd'+ str(i['i']+1) + str(j['j']+1) + '32'
            left='intd'+ str(i['i']+1) + str(j['j']+1) + '21'
            right='intd'+ str(i['i']+1) + str(j['j']+1) + '23'
            name='intd'+ str(i['i']+1) + str(j['j']+1) + '22'
            emit('putCardGraphic', {'tableID':tableID,'color':turns[session.get('room')],'cardtop':actualCard[room][0].top,'cardbot':actualCard[room][0].bot,'cardleft':actualCard[room][0].left,'cardright':actualCard[room][0].right,'cardname':actualCard[room][0].name,'i':i,'j':j,'top':top,'bot':bot,'left':left,'right':right,'name':name},room=room)
            top='intd'+ str(actualCard[room][1]+1) + '12'
            bot='intd'+ str(actualCard[room][1]+1) + '32'
            left='intd'+ str(actualCard[room][1]+1) + '21'
            right='intd'+ str(actualCard[room][1]+1) + '23'
            name='intd'+ str(actualCard[room][1]+1) + '22'
            hands[player][actualCard[room][1]]=decks[session.get('player')].pop(randrange(len(decks[session.get('player')])))
            print(decks[session.get('player')])
            emit('cardChange',{'cardtop':hands[player][actualCard[room][1]].top,'cardbot':hands[player][actualCard[room][1]].bot,'cardleft':hands[player][actualCard[room][1]].left,'cardright':hands[player][actualCard[room][1]].right,'cardname':hands[player][actualCard[room][1]].name,'top':top,'bot':bot,'left':left,'right':right,'name':name},player=session.get('player'))
            
            
            try:
                if boards[room,i['i'],j['j']][0].top>boards[room,i['i']-1,j['j']][0].bot:
                    boards[room,i['i']-1,j['j']][1]=turns[room]
                    tableID = 'tabl' + str(i['i']) + str(j['j']+1)
                    emit('boardChange',{'tableID':tableID,'color':turns[room]},room=room)
            except:
                pass
            try:
                if boards[room,i['i'],j['j']][0].bot>boards[room,i['i']+1,j['j']][0].top:
                    boards[room,i['i']+1,j['j']][1]=turns[room]
                    tableID = 'tabl' + str(i['i']+2) + str(j['j']+1)
                    emit('boardChange',{'tableID':tableID,'color':turns[room]},room=room)
            except:
                pass
            try:
                if boards[room,i['i'],j['j']][0].left>boards[room,i['i'],j['j']-1][0].right:
                    boards[room,i['i'],j['j']-1][1]=turns[room]
                    tableID = 'tabl' + str(i['i']+1) + str(j['j'])
                    emit('boardChange',{'tableID':tableID,'color':turns[room]},room=room)
            except:
                pass
            try:
                if boards[room,i['i'],j['j']][0].right>boards[room,i['i'],j['j']+1][0].left:
                    boards[room,i['i'],j['j']+1][1]=turns[room]
                    tableID = 'tabl' + str(i['i']+1) + str(j['j']+2)
                    emit('boardChange',{'tableID':tableID,'color':turns[room]},room=room)
            except:
                pass
            
            
            db[room]+=1
            phases[room]='select'
            if turns[room]=='green':
                turns[room]='red'
            else:
                turns[room]='green'
                
            if db[room]>24:
                red=0
                green=0
                for k in range(5):
                    for l in range(5):
                        if boards[room,k,l][1]=='red':
                            red+=1
                        elif boards[room,k,l][1]=='green':
                            green+=1
                if red>green:
                    emit('message', {'msg': 'Red player won the game Congratulate, please leave the room.'}, room=room)
                else:
                    emit('message', {'msg': 'Green player won the game Congratulate, please leave the room.'}, room=room)
                    
        #green player
        if player == clientsInRoom[room][1]-1 and turns[session.get('room')]=='green' and (room,i['i'],j['j']) not in boards:
            boards[room,i['i'],j['j']]=[actualCard[room][0],turns[room]]
            tableID = 'tabl' + str(i['i']+1) + str(j['j']+1)
            top='intd'+ str(i['i']+1) + str(j['j']+1) + '12'
            bot='intd'+ str(i['i']+1) + str(j['j']+1) + '32'
            left='intd'+ str(i['i']+1) + str(j['j']+1) + '21'
            right='intd'+ str(i['i']+1) + str(j['j']+1) + '23'
            name='intd'+ str(i['i']+1) + str(j['j']+1) + '22'
            emit('putCardGraphic', {'tableID':tableID,'color':turns[session.get('room')],'cardtop':actualCard[room][0].top,'cardbot':actualCard[room][0].bot,'cardleft':actualCard[room][0].left,'cardright':actualCard[room][0].right,'cardname':actualCard[room][0].name,'i':i,'j':j,'top':top,'bot':bot,'left':left,'right':right,'name':name},room=room)
            top='intd'+ str(actualCard[room][1]+1) + '12'
            bot='intd'+ str(actualCard[room][1]+1) + '32'
            left='intd'+ str(actualCard[room][1]+1) + '21'
            right='intd'+ str(actualCard[room][1]+1) + '23'
            name='intd'+ str(actualCard[room][1]+1) + '22'
            hands[player][actualCard[room][1]]=decks[session.get('player')].pop(randrange(len(decks[session.get('player')])))
            print(decks[session.get('player')])
            emit('cardChange',{'cardtop':hands[player][actualCard[room][1]].top,'cardbot':hands[player][actualCard[room][1]].bot,'cardleft':hands[player][actualCard[room][1]].left,'cardright':hands[player][actualCard[room][1]].right,'cardname':hands[player][actualCard[room][1]].name,'top':top,'bot':bot,'left':left,'right':right,'name':name},player=session.get('player'))
            
            
            try:
                if boards[room,i['i'],j['j']][0].top>boards[room,i['i']-1,j['j']][0].bot:
                    boards[room,i['i']-1,j['j']][1]=turns[room]
                    tableID = 'tabl' + str(i['i']) + str(j['j']+1)
                    emit('boardChange',{'tableID':tableID,'color':turns[room]},room=room)
            except:
                pass
            try:
                if boards[room,i['i'],j['j']][0].bot>boards[room,i['i']+1,j['j']][0].top:
                    boards[room,i['i']+1,j['j']][1]=turns[room]
                    tableID = 'tabl' + str(i['i']+2) + str(j['j']+1)
                    emit('boardChange',{'tableID':tableID,'color':turns[room]},room=room)
            except:
                pass
            try:
                if boards[room,i['i'],j['j']][0].left>boards[room,i['i'],j['j']-1][0].right:
                    boards[room,i['i'],j['j']-1][1]=turns[room]
                    tableID = 'tabl' + str(i['i']+1) + str(j['j'])
                    emit('boardChange',{'tableID':tableID,'color':turns[room]},room=room)
            except:
                pass
            try:
                if boards[room,i['i'],j['j']][0].right>boards[room,i['i'],j['j']+1][0].left:
                    boards[room,i['i'],j['j']+1][1]=turns[room]
                    tableID = 'tabl' + str(i['i']+1) + str(j['j']+2)
                    emit('boardChange',{'tableID':tableID,'color':turns[room]},room=room)
            except:
                pass
            
            
            db[room]+=1
            phases[room]='select'
            if turns[room]=='green':
                turns[room]='red'
            else:
                turns[room]='green'
                
            if db[room]>24:
                red=0
                green=0
                for k in range(5):
                    for l in range(5):
                        if boards[room,k,l][1]=='red':
                            red+=1
                        elif boards[room,k,l][1]=='green':
                            green+=1
                if red>green:
                    emit('message', {'msg': 'Red player won the game Congratulate, please leave the room.'}, room=room)
                else:
                    emit('message', {'msg': 'Green player won the game Congratulate, please leave the room.'}, room=room)
        
        else:
            pass
    else:
        pass

@socketio.on('changeColor', namespace='/chat')
def changeColor(i):
    room = session.get('room')
    print(i)
    if i['i']==1:
        color="red"
    elif i['i']==2:
        color="green"
    elif i['i']==0:
        color="pink"
    else:
        color="pink"
    emit('changeColor2', {'color':color}, room=room)
    
@socketio.on('requestInitHand', namespace='/chat')
def initHand():
    player = session.get('player')-1
    emit('recieveInitHand', {'card1top':hands[player][0].top,'card1bot':hands[player][0].bot,'card1left':hands[player][0].left,'card1right':hands[player][0].right,'card1name':hands[player][0].name,'card2top':hands[player][1].top,'card2bot':hands[player][1].bot,'card2left':hands[player][1].left,'card2right':hands[player][1].right,'card2name':hands[player][1].name,'card3top':hands[player][2].top,'card3bot':hands[player][2].bot,'card3left':hands[player][2].left,'card3right':hands[player][2].right,'card3name':hands[player][2].name,'card4top':hands[player][3].top,'card4bot':hands[player][3].bot,'card4left':hands[player][3].left,'card4right':hands[player][3].right,'card4name':hands[player][3].name}, player=player)
    
    