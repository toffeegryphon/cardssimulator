#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import websockets
import json
import logging

STATE = {"value": 0}
USERS = set()

def state_event():
    return json.dumps({"type": "state", **STATE})

def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})

async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def register(websocket):
    USERS.add(websocket)
    await notify_users()

async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()

async def server(websocket, path):
    print("Waiting...")
    await register(websocket)

    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            print(json.dumps(message))
            STATE['value'] = message
            await notify_state()
            #  except:
                #  logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)

start_server = websockets.serve(server, 'localhost', 1337)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
