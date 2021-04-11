#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import backend.server as server
import backend.core as core

import eventlet

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), server.server.app)
