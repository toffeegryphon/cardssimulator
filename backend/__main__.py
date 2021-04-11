#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import backend.server as server
import backend.core as core

from aiohttp import web

if __name__ == '__main__':
    server.server.run()
