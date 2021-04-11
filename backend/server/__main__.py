#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socketio
from server.core.game_instance import GameInstance
from . import sio, app

playerList = {}

def get_players(rid: str):
    return playerList[rid]['players']

def get_instance(rid: str):
    return playerList[rid]['instance']

@sio.event
def connect(sid, environ):
    print("connect ", sid)
    

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    # TODO leave room

@sio.on('join')
def on_join(sid, data: str):
    rid = data['rid']
    sio.enter_room(sid, rid)
    if not playerList.get(rid, None):
        playerList[rid] = {'players': [sid], 'instance': GameInstance()}
    else:
        get_players(rid).append(sid)
    #  playerList.setdefault(rid, { 'players': [], 'instance': GameInstance()})['players'].append(sid)
    get_instance(rid).addPlayer(sid, data['name'])
    #  print(playerList)
    #  print(get_instance(rid).players)
    return rid

@sio.on('initialize')
async def on_initialize(sid, data: dict):
    rid = data['rid']
    broadcast = get_instance(rid).initialize(get_players(rid))
    #  print(broadcast)
    await sio.emit('update', broadcast, room=data['rid'])

@sio.on('play')
async def on_play(sid, data: dict):
    response, broadcast = playerList[data['rid']]['instance'].play(sid, data['target'], data['value'])
    #  print(data)
    #  print(broadcast)
    await sio.emit('update', broadcast, room=data['rid'])
    return response

@sio.on('shuffle')
async def on_shuffle(sid, data: dict):
    pass

@sio.on('draw')
async def on_draw(sid, data: dict):
    rid = data['rid']
    response, broadcast = get_instance(rid).draw(sid, data['count'])

    await sio.emit('update', broadcast, room = rid)
    return response

@sio.on('deal')
async def on_deal(sid, data: dict):
    rid = data['rid']
    broadcast, state = get_instance(rid).deal(data['count'])
    #  print(broadcast)
    for pid in broadcast:
        message = broadcast[pid]
        #  print(message)
        message['state'] = state
        await sio.emit('update', message, room=pid)
    

#  app.router.add_static('/static', 'static')
#  app.router.add_get('/', index)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    
