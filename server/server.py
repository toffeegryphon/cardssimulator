#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
import socketio
from ..core.game_instance import GameInstance

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)
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
    playerList.setdefault(rid, { 'players': [], 'instance': GameInstance()})['players'].append(sid)
    get_instance(rid).addPlayer(sid, data['name'])
    return rid

@sio.on('initialize')
async def on_initialize(sid, data: dict):
    rid = data['rid']
    broadcast = get_instance(rid).initialize(get_players(rid))
    print(broadcast)
    await sio.emit('update', broadcast, room=data['rid'])

@sio.on('play')
async def on_play(sid, data: dict):
    response, broadcast = playerList[data['rid']]['instance'].play(sid, data['target'], data['value'])
    print(data)
    print(broadcast)
    await sio.emit('update', broadcast, room=data['rid'])
    return response
    # await sio.emit('update', { 'action': 'add', **data }, room=data['rid'])
    # return { 'action': 'remove', 'value': data['value']}

@sio.on('shuffle')
async def on_shuffle(sid, data: dict):
    pass
         
            
    
    

@sio.on('deal')
async def on_deal(sid, data: dict):
    print(playerList)
    rid = data['rid']
    broadcast, state = get_instance(rid).deal(data['count'])
    print(broadcast)
    for pid in broadcast:
        message = broadcast[pid]
        message['state'] = state
        await sio.emit('update', message, room=rid)
    

#  app.router.add_static('/static', 'static')
#  app.router.add_get('/', index)

def run():
    web.run_app(app)

#  if __name__ == '__main__':
    #  web.run_app(app)

