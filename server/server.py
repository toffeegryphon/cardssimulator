#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
import socketio
from ..core.game_instance import GameInstance

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)
playerList = {}

@sio.event
def connect(sid, environ):
    print("connect ", sid)
    

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.on('join')
def on_join(sid, rid: str):
    sio.enter_room(sid, rid)
    playerList.setdefault(rid, { 'players': [], 'instance': GameInstance()})['players'].append(sid)
    return rid

@sio.on('play')
async def on_play(sid, data: dict):
    print(data)
    response, broadcast = playerList[data['rid']]['instance'].play(sid, data['target'], data['value'])
    await sio.emit('update', broadcast, room=data['rid'])
    return response
    # await sio.emit('update', { 'action': 'add', **data }, room=data['rid'])
    # return { 'action': 'remove', 'value': data['value']}

@sio.on('shuffle')
async def on_shuffle(sid, data: dict):
    pass
         
            
    
    

@sio.on('deal')
async def on_deal(sid, data: dict):
    for i in playerList[data['rid']]['players']:
        await sio.emit('update', { 'action': 'add', **data }, room= i)
    

#  app.router.add_static('/static', 'static')
#  app.router.add_get('/', index)

def run():
    web.run_app(app)

#  if __name__ == '__main__':
    #  web.run_app(app)

