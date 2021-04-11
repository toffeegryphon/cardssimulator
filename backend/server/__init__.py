#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketio

sio = socketio.Server(async_mode='gevent_uwsgi', cors_allowed_origins='*',
                           logger=True, engineio_logger=True)


from server.core.game_instance import GameInstance

playerList = {}

def get_players(rid: str):
    return playerList[rid]['players']

def get_instance(rid: str):
    return playerList[rid]['instance']

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    roomId = None
    for rid in playerList:
        if sid in get_players(rid):
            roomId = rid
            playerList[rid]['players'].remove(sid)
            get_instance(rid).removePlayer(sid)
    sio.emit('update', {'action': 'none', 'state': get_instance(roomId).getState()})

@sio.on('join')
def on_join(sid, data: str):
    rid = data['rid']
    sio.enter_room(sid, rid)
    if not playerList.get(rid, None):
        playerList[rid] = {'players': [sid], 'instance': GameInstance()}
    else:
        get_players(rid).append(sid)
    instance = get_instance(rid)
    instance.addPlayer(sid, data['name'])
    state = instance.getState()
    data = {'action': 'none', 'state': state}
    sio.emit('update', data, room=rid)
    return {
        'rid': rid,
        'sid': sid,
        'target': '_field',
        'value': instance.getField(),
        'state': state
    }

@sio.on('initialize')
def on_initialize(sid, data: dict):
    rid = data['rid']
    broadcast = get_instance(rid).initialize(get_players(rid))
    #  print(broadcast)
    sio.emit('update', broadcast, room=data['rid'])
    return

@sio.on('refresh')
def on_refresh(sid, data: dict):
    rid = data['rid']
    instance = get_instance(rid)
    state = instance.getState()
    return {
        'rid': rid,
        'sid': sid,
        'target': '_field',
        'value': instance.getField(),
        'state': state
    }

@sio.on('play')
def on_play(sid, data: dict):
    response, broadcast = playerList[data['rid']]['instance'].play(sid, data['target'], data['value'])
    #  print(data)
    #  print(broadcast)
    sio.emit('update', broadcast, room=data['rid'])
    return response

@sio.on('shuffle')
def on_shuffle(sid, data: dict):
    pass

@sio.on('draw')
def on_draw(sid, data: dict):
    rid = data['rid']
    response, broadcast = get_instance(rid).draw(sid, data['count'])

    sio.emit('update', broadcast, room = rid)
    return response

@sio.on('deal')
def on_deal(sid, data: dict):
    rid = data['rid']
    broadcast, state = get_instance(rid).deal(data['count'])
    #  print(broadcast)
    for pid in broadcast:
        message = broadcast[pid]
        #  print(message)
        message['state'] = state
        sio.emit('update', message, room=pid)
app = socketio.WSGIApp(sio)

