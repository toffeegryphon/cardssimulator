#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  from . import server
import socketio
#  from server.core.game_instance import GameInstance

sio = socketio.Server(async_mode='eventlet')
app = socketio.WSGIApp(sio)
import eventlet
eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
