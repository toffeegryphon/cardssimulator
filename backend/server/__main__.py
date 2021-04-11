#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
import socketio

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

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
    return rid

@sio.on('play')
async def on_play(sid, data: dict):
    print(data)
    await sio.emit('update', { 'action': 'add', **data }, room=data['rid'])
    return { 'action': 'remove', 'value': data['value']}

#  app.router.add_static('/static', 'static')
#  app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)

