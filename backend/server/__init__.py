#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketio
import tornado

sio = socketio.AsyncServer(async_mode='tornado', cors_allowed_origins='*')

app = tornado.web.Application(
    [
        (r'/socket.io/', socketio.get_tornado_handler(sio))
    ]
)
