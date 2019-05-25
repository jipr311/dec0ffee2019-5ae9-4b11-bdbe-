#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"hablame!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

'''
from simple_websocket_server import WebSocketServer, WebSocket


class SimpleEcho(WebSocket):
	def handle(self):
		print("new msg: " + self.data)
		self.send_message("queloque!")

	def connected(self):
		print(self.address, 'connected')

	def handle_close(self):
		print(self.address, 'closed')


server = WebSocketServer('', 8765, SimpleEcho)
server.serve_forever()
