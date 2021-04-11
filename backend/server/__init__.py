#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  from . import server
from aiohttp import web
import socketio
from server.core.game_instance import GameInstance

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
